# 🧠 MNIST AI Web Application

A complete handwritten digit recognition web application built with **PyTorch, FastAPI, HTML, CSS, JavaScript, Git, and GitHub**.

This project demonstrates a complete Machine Learning workflow from project initialization and Git version control to neural network training, model saving, REST API development, and web-based inference.

---

# 📌 Project Workflow

The project was developed in the following order:

```text
Create Project
      ↓
Initialize Git
      ↓
Create Virtual Environment
      ↓
Install Dependencies
      ↓
Create Neural Network
      ↓
Train MNIST Model
      ↓
Evaluate Model
      ↓
Save model.pth
      ↓
Create FastAPI Backend
      ↓
Test REST API
      ↓
Create Frontend
      ↓
Connect Frontend to API
      ↓
Test Complete Application
      ↓
Commit Changes
      ↓
Push to GitHub
```

---

# ✨ Features

* PyTorch Convolutional Neural Network
* MNIST handwritten digit classification
* Model training
* Model evaluation
* Saved PyTorch model
* FastAPI REST API
* Swagger API documentation
* Image upload
* Prediction confidence
* HTML/CSS/JavaScript frontend
* Python virtual environment
* Git version control
* GitHub repository

---

# 📊 Model Performance

The trained model achieved:

| Metric           |     Result |
| ---------------- | ---------: |
| Dataset          |      MNIST |
| Training samples |     60,000 |
| Test samples     |     10,000 |
| Epochs           |          5 |
| Test Accuracy    | **99.10%** |
| Model format     |     `.pth` |

Training result:

```text
Epoch 4 completed | Average Loss: 0.0339

Epoch 5 completed | Average Loss: 0.0271

Evaluating model...
==================================================
Test Accuracy: 99.10%
==================================================

Model saved as:
backend/model.pth
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
* Git
* GitHub
* MNIST

---

# 💻 Requirements

Recommended:

```text
Windows 10/11
Python 3.x 64-bit
Git
VS Code
Internet connection for downloading MNIST
```

---

# 🚀 COMPLETE PROJECT SETUP FROM ZERO

The following section documents the complete process used to build the project.

---

# STEP 1 — Create the Project Directory

Open PowerShell.

Create the project folder:

```powershell
mkdir mnist-web-app
```

Enter the project:

```powershell
cd mnist-web-app
```

Verify:

```powershell
pwd
```

---

# STEP 2 — Initialize Git Immediately

Git should be initialized at the beginning of the project.

Run:

```powershell
git init
```

Expected:

```text
Initialized empty Git repository
```

Check:

```powershell
git status
```

At this point the project is already under Git version control.

---

# STEP 3 — Configure Git

Set your Git username:

```powershell
git config --global user.name "Ali Zeydi Abdian"
```

Set your Git email:

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

# STEP 4 — Create the Virtual Environment

Create the Python virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

The terminal should now show:

```text
(.venv)
```

Example:

```text
(.venv) PS C:\...\mnist-web-app>
```

---

# STEP 5 — Configure `.gitignore`

Create:

```text
.gitignore
```

Use:

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo

# Virtual environments
.venv/
venv/
env/

# Jupyter
.ipynb_checkpoints/

# VS Code
.vscode/

# Dataset
data/

# Logs
*.log

# OS
.DS_Store
Thumbs.db
```

This prevents unnecessary files from entering Git.

Especially:

```text
.venv/
```

must not be committed.

---

# STEP 6 — Create the Initial Project Structure

Create:

```text
backend/
frontend/
```

The project should now look like:

```text
mnist-web-app/
│
├── .venv/
│
├── backend/
│
├── frontend/
│
└── .gitignore
```

---

# STEP 7 — Create Backend Files

Inside `backend`, create:

```text
backend/
├── model.py
├── train.py
└── requirements.txt
```

Later we will add:

```text
main.py
model.pth
```

---

# STEP 8 — Install Python Dependencies

Move to backend:

```powershell
cd backend
```

Install PyTorch:

```powershell
pip install torch torchvision torchaudio
```

Install FastAPI:

```powershell
pip install fastapi uvicorn python-multipart pillow
```

Save dependencies:

```powershell
pip freeze > requirements.txt
```

---

# STEP 9 — Verify PyTorch

Check PyTorch:

```powershell
python -c "import torch; print(torch.__version__)"
```

Check CUDA:

```powershell
python -c "import torch; print(torch.cuda.is_available())"
```

Possible output:

```text
True
```

or:

```text
False
```

The application can run on CPU or CUDA.

---

# STEP 10 — Create the Neural Network

Create:

```text
backend/model.py
```

This file contains the CNN architecture.

The model receives:

```text
28 × 28 grayscale image
```

and predicts one of:

```text
0 1 2 3 4 5 6 7 8 9
```

---

# STEP 11 — Create Training Script

Create:

```text
backend/train.py
```

The training script:

1. Downloads MNIST
2. Loads training data
3. Loads test data
4. Creates the CNN
5. Trains for 5 epochs
6. Evaluates the model
7. Saves the trained model

---

# STEP 12 — Train the Model

From:

```text
mnist-web-app/backend
```

run:

```powershell
python train.py
```

Training output should look similar to:

```text
Epoch [1/5]
Epoch [2/5]
Epoch [3/5]
Epoch [4/5]
Epoch [5/5]
```

At the end:

```text
Evaluating model...
Test Accuracy: 99.10%
```

The model is saved as:

```text
backend/model.pth
```

---

# STEP 13 — Verify the Model

Check:

```powershell
Get-Item .\model.pth
```

Check model size:

```powershell
Get-Item .\model.pth |
Select-Object Name,@{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}
```

---

# STEP 14 — First Git Checkpoint

At this point the project has meaningful content.

Go back to project root:

```powershell
cd ..
```

Check:

```powershell
git status
```

Add files:

```powershell
git add .
```

Create the first commit:

```powershell
git commit -m "Add MNIST model training pipeline"
```

This creates a checkpoint containing the initial ML implementation.

---

# STEP 15 — Create FastAPI Backend

Create:

```text
backend/main.py
```

The API loads:

```text
backend/model.pth
```

and exposes:

```text
POST /predict
```

The API performs:

```text
Upload Image
      ↓
Grayscale
      ↓
Resize 28×28
      ↓
Tensor
      ↓
Normalization
      ↓
CNN
      ↓
Prediction
```

---

# STEP 16 — Run FastAPI

Enter backend:

```powershell
cd backend
```

Run:

```powershell
uvicorn main:app --reload
```

The API should be available at:

```text
http://127.0.0.1:8000
```

Keep this terminal open.

---

# STEP 17 — Test FastAPI

Open:

```text
http://127.0.0.1:8000
```

Test health:

```text
http://127.0.0.1:8000/health
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# STEP 18 — Test `/predict`

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

Select a digit image.

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

# STEP 19 — Create Frontend

Create:

```text
frontend/
├── index.html
├── style.css
└── app.js
```

The frontend provides:

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

# STEP 20 — Run the Frontend

Keep FastAPI running.

Open another terminal.

Go to frontend:

```powershell
cd C:\Users\Microsoft\Desktop\mnist-web-app\frontend
```

Run:

```powershell
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

---

# STEP 21 — Test the Complete Application

The final workflow is:

```text
User
 ↓
Select Image
 ↓
Frontend
 ↓
POST /predict
 ↓
FastAPI
 ↓
Image Preprocessing
 ↓
MNISTCNN
 ↓
Prediction
 ↓
JSON
 ↓
Frontend
 ↓
Digit + Confidence
```

Example:

```text
Prediction

7

Confidence: 99.12%
```

---

# STEP 22 — Check Git Status

Stop the servers if necessary using:

```text
Ctrl + C
```

Return to the project root:

```powershell
cd C:\Users\Microsoft\Desktop\mnist-web-app
```

Check:

```powershell
git status
```

---

# STEP 23 — Add the README

Create:

```text
README.md
```

Add the project documentation.

Then:

```powershell
git add README.md
```

---

# STEP 24 — Commit the Complete Application

Commit:

```powershell
git add .
```

Then:

```powershell
git commit -m "Complete MNIST web application"
```

Check history:

```powershell
git log --oneline
```

You should see commits similar to:

```text
xxxxxxxx Complete MNIST web application
xxxxxxxx Add MNIST model training pipeline
```

---

# STEP 25 — Create GitHub Repository

Open GitHub:

https://github.com

Create a new repository:

```text
mnist-web-app
```

Recommended:

```text
Public
```

Do NOT initialize it with:

```text
README
.gitignore
License
```

because these already exist locally.

---

# STEP 26 — Connect Local Git to GitHub

Repository:

```text
https://github.com/Aliyar4061/mnist-web-app
```

Run:

```powershell
git remote add origin https://github.com/Aliyar4061/mnist-web-app.git
```

Verify:

```powershell
git remote -v
```

Expected:

```text
origin  https://github.com/Aliyar4061/mnist-web-app.git (fetch)
origin  https://github.com/Aliyar4061/mnist-web-app.git (push)
```

---

# STEP 27 — Rename Main Branch

Use:

```powershell
git branch -M main
```

Verify:

```powershell
git branch
```

Expected:

```text
* main
```

---

# STEP 28 — First Push to GitHub

Push the complete project:

```powershell
git push -u origin main
```

Expected:

```text
[new branch] main -> main
branch 'main' set up to track 'origin/main'
```

Repository:

https://github.com/Aliyar4061/mnist-web-app

---

# STEP 29 — Verify the Remote Repository

Check remote branches:

```powershell
git ls-remote --heads origin
```

Expected:

```text
refs/heads/main
```

Check status:

```powershell
git status
```

Expected:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

# 🔄 FUTURE DEVELOPMENT WORKFLOW

After the project has been uploaded to GitHub, use the following workflow every time you make changes.

---

# STEP 30 — Start the Project Again

Open PowerShell.

Go to the project:

```powershell
cd C:\Users\Microsoft\Desktop\mnist-web-app
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

---

# STEP 31 — Update the Local Repository

Before starting new development:

```powershell
git pull
```

This retrieves the latest version from GitHub.

---

# STEP 32 — Make Your Changes

Examples:

```text
Modify model.py
Modify train.py
Modify main.py
Modify index.html
Modify style.css
Modify app.js
```

Test everything locally.

---

# STEP 33 — Check Changes

```powershell
git status
```

See exact changes:

```powershell
git diff
```

---

# STEP 34 — Add Changes

Add everything:

```powershell
git add .
```

Or add a specific file:

```powershell
git add backend/main.py
```

---

# STEP 35 — Create a Commit

Use a meaningful message.

Example:

```powershell
git commit -m "Improve API prediction handling"
```

Other examples:

```powershell
git commit -m "Improve frontend interface"
```

```powershell
git commit -m "Update MNIST model"
```

```powershell
git commit -m "Add prediction confidence display"
```

---

# STEP 36 — Push Changes

After committing:

```powershell
git push
```

The changes are now uploaded to GitHub.

---

# 🔁 STANDARD DAILY GIT WORKFLOW

For normal development, use:

```powershell
git pull
```

Make changes.

Then:

```powershell
git status
```

```powershell
git add .
```

```powershell
git commit -m "Describe your changes"
```

```powershell
git push
```

In short:

```text
git pull
   ↓
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

# 🌿 Git Branch Management

Create a new branch:

```powershell
git checkout -b feature/canvas
```

Work on the feature.

Then:

```powershell
git add .
```

```powershell
git commit -m "Add drawing canvas"
```

Push:

```powershell
git push -u origin feature/canvas
```

Return to main:

```powershell
git checkout main
```

Update main:

```powershell
git pull
```

---

# 📜 Useful Git Commands

Check status:

```powershell
git status
```

View commits:

```powershell
git log --oneline
```

View latest commit:

```powershell
git log --oneline -1
```

View branches:

```powershell
git branch
```

View remote:

```powershell
git remote -v
```

View differences:

```powershell
git diff
```

Download latest changes:

```powershell
git pull
```

Upload changes:

```powershell
git push
```

Stage all changes:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Commit message"
```

---

# 🧠 Retraining the Model

If you change the neural network or training parameters:

```powershell
cd C:\Users\Microsoft\Desktop\mnist-web-app
.venv\Scripts\Activate.ps1
cd backend
```

Train:

```powershell
python train.py
```

Verify:

```powershell
Get-Item .\model.pth
```

Return to root:

```powershell
cd ..
```

Check:

```powershell
git status
```

If `model.pth` changed:

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

# 📦 Requirements Management

If dependencies change:

```powershell
pip install package-name
```

Update requirements:

```powershell
pip freeze > backend/requirements.txt
```

Then:

```powershell
git add backend/requirements.txt
```

```powershell
git commit -m "Update Python dependencies"
```

```powershell
git push
```

---

# 🔐 `.gitignore`

The following should not normally be uploaded:

```text
.venv/
__pycache__/
data/
.ipynb_checkpoints/
.vscode/
*.log
```

Never commit:

```text
API keys
Passwords
Access tokens
Private keys
Credentials
Secrets
```

If environment variables are introduced later, add:

```text
.env
```

to `.gitignore`.

---

# 📦 Model File

The trained model is:

```text
backend/model.pth
```

Check its size:

```powershell
Get-Item .\backend\model.pth |
Select-Object Name,@{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}
```

The current model is small enough for the current project.

For substantially larger models, Git LFS should be considered.

---

# 🛑 Stop the Servers

FastAPI:

```text
Ctrl + C
```

Frontend:

```text
Ctrl + C
```

---

# 🔌 API Reference

## GET `/`

Returns API information.

Example:

```json
{
    "message": "MNIST Digit Recognition API is running",
    "model": "MNISTCNN",
    "device": "cpu"
}
```

---

## GET `/health`

Checks API and model status.

Example:

```json
{
    "status": "ok",
    "model_loaded": true,
    "device": "cpu"
}
```

---

## POST `/predict`

Accepts an image and returns the predicted digit.

Request:

```text
POST /predict
Content-Type: multipart/form-data
```

Parameter:

```text
file
```

Example:

```json
{
    "prediction": 7,
    "confidence": 0.9987,
    "filename": "seven.png"
}
```

---

# 🌐 Local URLs

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

Health:

```text
http://127.0.0.1:8000/health
```

Frontend:

```text
http://127.0.0.1:5500
```

GitHub:

```text
https://github.com/Aliyar4061/mnist-web-app
```

---

# 📁 Final Project Structure

```text
mnist-web-app/
│
├── .venv/
│
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── model.pth
│   ├── requirements.txt
│   └── train.py
│
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── style.css
│
├── .gitignore
│
└── README.md
```

---

# 🧪 Complete Reproduction Procedure

If you want to rebuild the project from scratch, the essential sequence is:

```powershell
mkdir mnist-web-app
cd mnist-web-app

git init

git config --global user.name "Ali Zeydi Abdian"
git config --global user.email "aabdian67@gmail.com"

python -m venv .venv
.venv\Scripts\Activate.ps1

mkdir backend
mkdir frontend
```

Create `.gitignore`.

Then:

```powershell
cd backend

pip install torch torchvision torchaudio
pip install fastapi uvicorn python-multipart pillow

pip freeze > requirements.txt
```

Create:

```text
model.py
train.py
```

Train:

```powershell
python train.py
```

Create:

```text
main.py
```

Run API:

```powershell
uvicorn main:app --reload
```

Test:

```text
http://127.0.0.1:8000/docs
```

Create:

```text
frontend/index.html
frontend/style.css
frontend/app.js
```

Run frontend:

```powershell
cd ../frontend
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

Then return to root:

```powershell
cd ..
```

Git:

```powershell
git status
git add .
git commit -m "Complete MNIST web application"
```

Connect GitHub:

```powershell
git remote add origin https://github.com/Aliyar4061/mnist-web-app.git
```

Set main:

```powershell
git branch -M main
```

Push:

```powershell
git push -u origin main
```

---

# 🎯 Final Architecture

```text
                         GitHub
                           │
                           │
                           ▼
                 ┌──────────────────┐
                 │  mnist-web-app   │
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
        ┌────────────┐          ┌────────────┐
        │  Backend   │          │  Frontend  │
        │            │          │            │
        │ PyTorch    │          │ HTML       │
        │ CNN        │          │ CSS        │
        │ FastAPI    │          │ JavaScript │
        └─────┬──────┘          └─────┬──────┘
              │                       │
              │       HTTP API        │
              └───────────┬───────────┘
                          │
                          ▼
                   ┌──────────────┐
                   │   MNIST CNN  │
                   │              │
                   │  model.pth   │
                   └──────┬───────┘
                          │
                          ▼
                 Digit Prediction
                          │
                          ▼
                  Confidence Score
```

---

# 🚧 Future Improvements

Possible next versions:

* Interactive drawing canvas
* Drag & drop upload
* Automatic image inversion
* Thresholding
* Image centering
* Noise removal
* Top-3 predictions
* Prediction probability chart
* Responsive mobile UI
* Docker deployment
* Cloud deployment
* Automated testing
* GitHub Actions CI/CD
* Production API configuration

---

# 👨‍💻 Author

**Ali Zeydi Abdian**

GitHub:

https://github.com/Aliyar4061

Project:

https://github.com/Aliyar4061/mnist-web-app

---

# 📜 License

This project is intended for educational and research purposes.
