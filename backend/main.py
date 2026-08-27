import io
from pathlib import Path

import torch

from PIL import Image

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from torchvision import transforms

from model import MNISTCNN


# =========================================================
# 1. FastAPI application
# =========================================================

app = FastAPI(
    title="MNIST Digit Recognition API",
    description="API for handwritten digit recognition using PyTorch",
    version="1.0.0"
)


# =========================================================
# 2. CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# =========================================================
# 3. Device
# =========================================================

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print("Device:", device)


# =========================================================
# 4. Load trained model
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "model.pth"


model = MNISTCNN().to(device)


model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=device
    )
)


model.eval()


print("Model loaded successfully!")
print("Model path:", MODEL_PATH)


# =========================================================
# 5. Image preprocessing
# =========================================================

transform = transforms.Compose([

    transforms.Grayscale(
        num_output_channels=1
    ),

    transforms.Resize(
        (28, 28)
    ),

    transforms.ToTensor(),

    transforms.Normalize(
        (0.1307,),
        (0.3081,)
    )
])


# =========================================================
# 6. Root endpoint
# =========================================================

@app.get("/")
def root():

    return {
        "message": "MNIST Digit Recognition API is running",
        "model": "MNISTCNN",
        "device": str(device)
    }


# =========================================================
# 7. Health check
# =========================================================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "model_loaded": True,
        "device": str(device)
    }


# =========================================================
# 8. Prediction endpoint
# =========================================================

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    # -----------------------------------------------------
    # Read uploaded file
    # -----------------------------------------------------

    image_bytes = await file.read()


    # -----------------------------------------------------
    # Convert bytes to PIL image
    # -----------------------------------------------------

    image = Image.open(
        io.BytesIO(image_bytes)
    )


    # -----------------------------------------------------
    # Preprocess image
    # -----------------------------------------------------

    image_tensor = transform(image)


    # -----------------------------------------------------
    # Add batch dimension
    # -----------------------------------------------------

    image_tensor = image_tensor.unsqueeze(0)


    # -----------------------------------------------------
    # Move to CPU/GPU
    # -----------------------------------------------------

    image_tensor = image_tensor.to(device)


    # -----------------------------------------------------
    # Model inference
    # -----------------------------------------------------

    with torch.no_grad():

        outputs = model(
            image_tensor
        )


        probabilities = torch.softmax(
            outputs,
            dim=1
        )


        confidence, prediction = torch.max(
            probabilities,
            dim=1
        )


    # -----------------------------------------------------
    # Return JSON response
    # -----------------------------------------------------

    return {

        "prediction": int(
            prediction.item()
        ),

        "confidence": float(
            confidence.item()
        ),

        "filename": file.filename
    }