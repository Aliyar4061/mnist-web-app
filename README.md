# MNIST AI Web Application

A complete handwritten digit recognition web application built with **PyTorch, FastAPI, HTML, CSS, and JavaScript**.

The application uses a Convolutional Neural Network (CNN) trained on the MNIST dataset and provides a REST API for image-based digit prediction.

---

## 🚀 Features

* PyTorch CNN for handwritten digit classification
* MNIST dataset
* 99.10% test accuracy
* Saved trained model (`model.pth`)
* FastAPI REST API
* Swagger API documentation
* Image upload from the web interface
* Prediction confidence score
* Simple HTML/CSS/JavaScript frontend
* Python virtual environment (`venv`)

---

## 🧠 Model Architecture

The model is a Convolutional Neural Network:

```text
Input
28 × 28 × 1
      │
      ▼
Conv2D
32 filters
      │
      ▼
ReLU
      │
      ▼
MaxPooling
      │
      ▼
Conv2D
64 filters
      │
      ▼
ReLU
      │
      ▼
MaxPooling
      │
      ▼
Flatten
      │
      ▼
Dense
128 neurons
      │
      ▼
Dropout
      │
      ▼
Dense
10 classes
      │
      ▼
0 ─ 1 ─ 2 ─ ... ─ 9
```

---

## 📊 Model Performance

The model was trained for 5 epochs using the Adam optimizer.

| Metric           |     Result |
| ---------------- | ---------: |
| Dataset          |      MNIST |
| Training samples |     60,000 |
| Test samples     |     10,000 |
| Epochs           |          5 |
| Optimizer        |       Adam |
| Test Accuracy    | **99.10%** |

---

# 📁 Project Structure

```text
mnist-web-app/
│
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── model.pth
│   ├── requirements.txt
│   └── train.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Aliyar4061/mnist-web-app.git
```

Enter the project directory:

```bash
cd mnist-web-app
```

---

## 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

at the beginning of your terminal.

---

## 3. Select the Python interpreter

In VS Code:

```text
Ctrl + Shift + P
```

Then select:

```text
Python: Select Interpreter
```

Choose:

```text
.venv\Scripts\python.exe
```

---

# 📦 Install Dependencies

Move into the backend directory:

```powershell
cd backend
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

---

# 🧠 Train the Model

If you want to retrain the model:

```powershell
python train.py
```

The MNIST dataset will be downloaded automatically.

After training, the trained model will be saved as:

```text
backend/model.pth
```

---

# 🚀 Run the Backend API

From the `backend` directory:

```powershell
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to upload an image and test the `/predict` endpoint.

---

# 🔮 Prediction API

Endpoint:

```text
POST /predict
```

The endpoint accepts an image file.

Example response:

```json
{
    "prediction": 7,
    "confidence": 0.9987,
    "filename": "seven.png"
}
```

The `prediction` field contains the recognized digit.

The `confidence` field represents the model confidence.

---

# 🌐 Run the Frontend

Keep the FastAPI server running.

Open another VS Code terminal.

Move to:

```powershell
cd frontend
```

Start a simple web server:

```powershell
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

---

# 🔄 Application Workflow

```text
User
 │
 │ Upload image
 ▼
Frontend
 │
 │ POST /predict
 ▼
FastAPI
 │
 ▼
Image preprocessing
 │
 ▼
MNISTCNN
 │
 │
 ▼
Prediction
 │
 ▼
JSON response
 │
 ▼
Frontend
 │
 ▼
Digit + Confidence
```

---

# 🛠️ Technologies

* Python
* PyTorch
* Torchvision
* FastAPI
* Uvicorn
* Pillow
* HTML5
* CSS3
* JavaScript
* REST API
* MNIST

---

# 📌 Notes

The model is trained on the MNIST dataset. MNIST images are grayscale handwritten digits with a resolution of 28×28 pixels.

For best prediction performance, uploaded images should resemble the MNIST image format.

Future versions can improve preprocessing by adding:

* Image inversion
* Automatic cropping
* Thresholding
* Centering
* Noise removal
* Canvas-based digit drawing

---

## 👨‍💻 Author

**Ali Zeydi Abdian**

GitHub:

https://github.com/Aliyar4061
