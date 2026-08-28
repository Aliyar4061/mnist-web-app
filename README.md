# 🧠 MNIST AI Web Application

A complete handwritten digit recognition web application built with **PyTorch, FastAPI, HTML, CSS, and JavaScript**.

This project demonstrates a complete machine learning deployment workflow:

```text
Dataset
   ↓
Neural Network Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
FastAPI REST API
   ↓
Frontend
   ↓
Image Upload
   ↓
AI Prediction
   ↓
Digit + Confidence
```

---

# 📌 Project Overview

This application uses a Convolutional Neural Network (CNN) trained on the **MNIST handwritten digit dataset**.

The trained model recognizes digits from:

```text
0 1 2 3 4 5 6 7 8 9
```

The trained model is saved as:

```text
backend/model.pth
```

The model is then loaded by a FastAPI backend and exposed through a REST API.

The frontend allows the user to upload an image and receive the prediction from the neural network.

---

# ✨ Features

* PyTorch CNN
* MNIST dataset
* Model training
* Model evaluation
* Saved trained model
* FastAPI REST API
* Swagger API documentation
* Image upload
* Prediction confidence
* HTML/CSS/JavaScript frontend
* Python virtual environment
* Git/GitHub version control

---

# 📊 Model Performance

The current trained model achieved:

| Metric           |         Result |
| ---------------- | -------------: |
| Dataset          |          MNIST |
| Training samples |         60,000 |
| Test samples     |         10,000 |
| Epochs           |              5 |
| Test Accuracy    |     **99.10%** |
| Model format     | PyTorch `.pth` |

Training output:

```text
Epoch 4 completed | Average Loss: 0.0339

Epoch 5 completed | Average Loss: 0.0271

Evaluating model...
==================================================
Test Accuracy: 99.10%
==================================================
```

---

# 📁 Project Structure

```text
mnist-web-app/
│
├── .venv/
│
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── train.py
│   ├── model.pth
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .gitignore
│
└── README.md
```

> `.venv/` is intentionally excluded from Git using `.gitignore`.

---

# 🧰 Technologies

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
* Git
* GitHub
* MNIST

---

# 💻 Requirements

Recommended environment:

```text
Windows 10/11
Python 3.10+
Git
VS Code
```

The project can also work with other supported Python versions depending on the installed PyTorch version.

---

# 🚀 Complete Setup From Zero

This section contains the complete command sequence needed to recreate and run the project.

---

# 1. Install Git

Install Git for Windows from:

https://git-scm.com/download/win

Verify the installation:

```powershell
git --version
```

Example:

```text
git version 2.x.x
```

---

# 2. Install Python

Check Python:

```powershell
python --version
```

Also check installed Python versions:

```powershell
py -0p
```

Check which Python executable is being used:

```powershell
where.exe python
```

> It is recommended to use a 64-bit Python installation for machine learning.

---

# 3. Clone the GitHub Repository

If the project already exists on GitHub:

```powershell
git clone https://github.com/Aliyar4061/mnist-web-app.git
```

Enter the project directory:

```powershell
cd mnist-web-app
```

Check the files:

```powershell
dir
```

---

# 4. Create Python Virtual Environment

From the project root:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv)
```

Example:

```text
(.venv) PS C:\Users\...\mnist-web-app>
```

---

# 5. If PowerShell Blocks Activation

If you receive an execution-policy error such as:

```text
running scripts is disabled on this system
```

run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Confirm with:

```text
Y
```

Then activate again:

```powershell
.venv\Scripts\Activate.ps1
```

---

# 6. Select Python Interpreter in VS Code

Open the project:

```powershell
code .
```

In VS Code:

```text
Ctrl + Shift + P
```

Select:

```text
Python: Select Interpreter
```

Choose:

```text
.venv\Scripts\python.exe
```

Verify from the terminal:

```powershell
python --version
```

---

# 7. Upgrade pip

With `.venv` activated:

```powershell
python -m pip install --upgrade pip
```

Verify:

```powershell
pip --version
```

---

# 8. Install Backend Dependencies

Enter backend:

```powershell
cd backend
```

Install requirements:

```powershell
pip install -r requirements.txt
```

If you want to verify the installed packages:

```powershell
pip list
```

---

# 9. Install Dependencies Manually

If `requirements.txt` is unavailable or needs to be recreated, install the main packages:

```powershell
pip install torch torchvision torchaudio
```

```powershell
pip install fastapi uvicorn python-multipart pillow
```

Then save the installed environment:

```powershell
pip freeze > requirements.txt
```

---

# 10. Verify PyTorch

Run:

```powershell
python -c "import torch; print(torch.__version__)"
```

Check CUDA availability:

```powershell
python -c "import torch; print(torch.cuda.is_available())"
```

If CUDA is available:

```text
True
```

If not:

```text
False
```

The application automatically uses:

```text
CUDA
```

when available, otherwise:

```text
CPU
```

---

# 11. Train the MNIST Model

From:

```text
mnist-web-app/backend
```

run:

```powershell
python train.py
```

The training process should display progress similar to:

```text
Epoch [1/5] ...
Epoch [2/5] ...
Epoch [3/5] ...
Epoch [4/5] ...
Epoch [5/5] ...
```

At the end:

```text
Evaluating model...
Test Accuracy: 99.10%
```

The trained model is saved as:

```text
backend/model.pth
```

---

# 12. Verify Model File

From the project root:

```powershell
Get-Item .\backend\model.pth
```

To check its size:

```powershell
Get-Item .\backend\model.pth |
Select-Object Name,@{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}
```

---

# 13. Run the FastAPI Backend

Make sure you are inside:

```text
mnist-web-app/backend
```

Run:

```powershell
uvicorn main:app --reload
```

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
```

Keep this terminal open.

---

# 14. Test the API

Open:

```text
http://127.0.0.1:8000
```

Expected response:

```json
{
    "message": "MNIST Digit Recognition API is running",
    "model": "MNISTCNN",
    "device": "cpu"
}
```

---

# 15. Test API Health

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
    "status": "ok",
    "model_loaded": true,
    "device": "cpu"
}
```

---

# 16. Open Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides an interactive API interface.

The main endpoint is:

```text
POST /predict
```

---

# 17. Test `/predict`

In Swagger:

```text
POST /predict
```

Click:

```text
Try it out
```

Then:

```text
Choose File
```

Select an image.

Click:

```text
Execute
```

Example response:

```json
{
    "prediction": 7,
    "confidence": 0.9987,
    "filename": "seven.png"
}
```

---

# 18. Run the Frontend

Do not close the FastAPI terminal.

Open a **new VS Code terminal**.

From the project root:

```powershell
cd frontend
```

Start the frontend web server:

```powershell
python -m http.server 5500
```

Expected output:

```text
Serving HTTP on :: port 5500
```

---

# 19. Open the Web Application

Open:

```text
http://127.0.0.1:5500
```

The application provides:

```text
Choose Image
      ↓
Image Preview
      ↓
Predict Digit
      ↓
FastAPI
      ↓
PyTorch CNN
      ↓
Prediction
      ↓
Confidence
```

---

# 🔌 API Architecture

The application uses the following architecture:

```text
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                             │ Upload Image
                             ▼
                    ┌──────────────────┐
                    │     Frontend     │
                    │ HTML/CSS/JS      │
                    └────────┬─────────┘
                             │
                             │ POST /predict
                             ▼
                    ┌──────────────────┐
                    │     FastAPI      │
                    │   Port: 8000     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Image Processing │
                    │ 28 × 28 Gray     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    MNISTCNN      │
                    │   model.pth      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Prediction    │
                    │ Digit + Confidence│
                    └──────────────────┘
```

---

# 🧠 Image Preprocessing

Uploaded images are processed using:

```text
Input Image
     ↓
Grayscale
     ↓
Resize 28 × 28
     ↓
Tensor
     ↓
Normalization
     ↓
CNN
```

MNIST images use:

```text
28 × 28
1 channel
Grayscale
```

---

# 📡 API Endpoint

## POST `/predict`

Request:

```text
POST http://127.0.0.1:8000/predict
```

Content type:

```text
multipart/form-data
```

Parameter:

```text
file
```

Example response:

```json
{
    "prediction": 7,
    "confidence": 0.9987,
    "filename": "seven.png"
}
```

---

# 🔄 Complete Workflow

```text
1. Install Python
       ↓
2. Install Git
       ↓
3. Clone Repository
       ↓
4. Create .venv
       ↓
5. Activate .venv
       ↓
6. Install requirements
       ↓
7. Train model
       ↓
8. Save model.pth
       ↓
9. Start FastAPI
       ↓
10. Test /docs
       ↓
11. Start frontend server
       ↓
12. Open web application
       ↓
13. Upload image
       ↓
14. Receive prediction
```

---

# 🌿 Git and GitHub Workflow

The following section contains the Git commands used to manage this project.

---

# 1. Initialize Git

If the project is not already a Git repository:

```powershell
git init
```

---

# 2. Configure Git Identity

Set your GitHub username:

```powershell
git config --global user.name "Ali Zeydi Abdian"
```

Set your email:

```powershell
git config --global user.email "aabdian67@gmail.com"
```

Verify:

```powershell
git config --global user.name
```

```powershell
git config --global user.email
```

---

# 3. Check Git Status

```powershell
git status
```

---

# 4. Add Files

Add all project files:

```powershell
git add .
```

Or add a specific file:

```powershell
git add README.md
```

---

# 5. Create a Commit

Initial commit:

```powershell
git commit -m "Initial MNIST AI web application"
```

For future changes:

```powershell
git commit -m "Update frontend"
```

or:

```powershell
git commit -m "Improve model inference"
```

---

# 6. Rename Branch to Main

```powershell
git branch -M main
```

---

# 7. Connect Local Repository to GitHub

Repository:

```text
https://github.com/Aliyar4061/mnist-web-app
```

Add remote:

```powershell
git remote add origin https://github.com/Aliyar4061/mnist-web-app.git
```

Check:

```powershell
git remote -v
```

Expected:

```text
origin  https://github.com/Aliyar4061/mnist-web-app.git (fetch)
origin  https://github.com/Aliyar4061/mnist-web-app.git (push)
```

---

# 8. Push the First Version

```powershell
git push -u origin main
```

After the first successful push, future pushes can normally use:

```powershell
git push
```

---

# 9. Check Remote Branches

```powershell
git ls-remote --heads origin
```

Expected:

```text
refs/heads/main
```

---

# 10. Normal Git Workflow After Making Changes

Whenever you modify the project:

```powershell
git status
```

Then:

```powershell
git add .
```

Then:

```powershell
git commit -m "Describe your changes"
```

Finally:

```powershell
git push
```

The normal cycle is:

```text
Modify
  ↓
git status
  ↓
git add .
  ↓
git commit
  ↓
git push
```

---

# 🔍 Useful Git Commands

Show commit history:

```powershell
git log --oneline
```

Show the latest commit:

```powershell
git log --oneline -1
```

Show remote:

```powershell
git remote -v
```

Show current branch:

```powershell
git branch
```

Check working tree:

```powershell
git status
```

Show changes:

```powershell
git diff
```

---

# 🚫 Files That Should NOT Be Uploaded

The following should normally remain outside Git:

```text
.venv/
__pycache__/
data/
```

They are excluded using:

```text
.gitignore
```

Do not manually upload the entire `.venv` directory.

---

# 📦 Model File

The trained model is:

```text
backend/model.pth
```

If the model is small enough, it can be stored directly in the repository.

Check its size:

```powershell
Get-Item .\backend\model.pth |
Select-Object Name,@{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}
```

If future model files become large, consider using **Git LFS**.

---

# 🔁 Retraining the Model

To retrain:

```powershell
cd backend
```

Then:

```powershell
python train.py
```

After training, verify:

```powershell
Get-Item .\model.pth
```

Return to project root:

```powershell
cd ..
```

Check changes:

```powershell
git status
```

If the model changed:

```powershell
git add backend/model.pth
```

Commit:

```powershell
git commit -m "Update trained MNIST model"
```

Push:

```powershell
git push
```

---

# 🛑 Stopping the Application

FastAPI runs in one terminal:

```text
uvicorn main:app --reload
```

Frontend runs in another:

```text
python -m http.server 5500
```

To stop either server:

```text
Ctrl + C
```

---

# 🧹 Deactivate Virtual Environment

When finished:

```powershell
deactivate
```

The:

```text
(.venv)
```

indicator will disappear.

---

# 🔄 Starting the Project Again

When returning to the project later:

```powershell
cd C:\Users\Microsoft\Desktop\mnist-web-app
```

Activate environment:

```powershell
.venv\Scripts\Activate.ps1
```

Start backend:

```powershell
cd backend
uvicorn main:app --reload
```

Open another terminal.

Start frontend:

```powershell
cd C:\Users\Microsoft\Desktop\mnist-web-app\frontend
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

---

# 🧪 Quick Start

For an already configured project, the shortest startup procedure is:

### Terminal 1 — Backend

```powershell
cd C:\Users\Microsoft\Desktop\mnist-web-app
.venv\Scripts\Activate.ps1
cd backend
uvicorn main:app --reload
```

### Terminal 2 — Frontend

```powershell
cd C:\Users\Microsoft\Desktop\mnist-web-app
.venv\Scripts\Activate.ps1
cd frontend
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500
```

---

# 🧩 Troubleshooting

## `python` command not found

Check:

```powershell
py -0p
```

You can also create the environment using:

```powershell
py -3 -m venv .venv
```

---

## Virtual environment does not activate

Run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
.venv\Scripts\Activate.ps1
```

---

## FastAPI cannot find `model.pth`

Make sure:

```text
backend/model.pth
```

exists.

Check:

```powershell
Get-Item .\model.pth
```

Run FastAPI from the backend directory:

```powershell
cd backend
uvicorn main:app --reload
```

---

## `ModuleNotFoundError`

Make sure `.venv` is activated:

```powershell
.venv\Scripts\Activate.ps1
```

Then:

```powershell
pip install -r backend\requirements.txt
```

---

## Frontend cannot connect to API

Make sure FastAPI is running:

```text
http://127.0.0.1:8000
```

Test:

```text
http://127.0.0.1:8000/health
```

Then start frontend:

```powershell
cd frontend
python -m http.server 5500
```

---

## Git Push fails

Check remote:

```powershell
git remote -v
```

It should be:

```text
https://github.com/Aliyar4061/mnist-web-app.git
```

Check branch:

```powershell
git branch
```

It should show:

```text
* main
```

Then:

```powershell
git push
```

---

# 🔐 Security

Do not commit sensitive information such as:

```text
API keys
Passwords
Access tokens
Private keys
.env files containing secrets
Credentials
```

If environment variables are introduced in future versions, add:

```text
.env
```

to `.gitignore`.

---

# 🚧 Future Improvements

Planned improvements include:

* Interactive drawing canvas
* Drag-and-drop image upload
* Automatic image inversion
* Image thresholding
* Automatic cropping
* Digit centering
* Noise removal
* Prediction probability chart
* Top-3 predictions
* Better responsive design
* Docker deployment
* Cloud deployment
* Production API configuration
* Automated testing
* CI/CD with GitHub Actions

---

# 📜 License

This project is intended for educational and research purposes.

---

# 👨‍💻 Author

**Ali Zeydi Abdian**

GitHub:

https://github.com/Aliyar4061

Project:

https://github.com/Aliyar4061/mnist-web-app
