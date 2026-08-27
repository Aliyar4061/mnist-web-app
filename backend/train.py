import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import DataLoader

from torchvision import datasets
from torchvision import transforms

from model import MNISTCNN


# ==========================================
# Configuration
# ==========================================

BATCH_SIZE = 64
EPOCHS = 5
LEARNING_RATE = 0.001


# ==========================================
# Device
# ==========================================

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print("=" * 50)
print("Device:", device)

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

print("=" * 50)


# ==========================================
# Transform
# ==========================================

transform = transforms.Compose([

    transforms.ToTensor(),

    transforms.Normalize(
        (0.1307,),
        (0.3081,)
    )
])


# ==========================================
# Dataset
# ==========================================

print("Downloading MNIST dataset...")


train_dataset = datasets.MNIST(
    root="../data",
    train=True,
    download=True,
    transform=transform
)


test_dataset = datasets.MNIST(
    root="../data",
    train=False,
    download=True,
    transform=transform
)


# ==========================================
# DataLoader
# ==========================================

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)


test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)


print("Training samples:", len(train_dataset))
print("Testing samples:", len(test_dataset))


# ==========================================
# Model
# ==========================================

model = MNISTCNN().to(device)


# ==========================================
# Loss
# ==========================================

criterion = nn.CrossEntropyLoss()


# ==========================================
# Optimizer
# ==========================================

optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)


# ==========================================
# Training
# ==========================================

print("\nStarting training...\n")


for epoch in range(EPOCHS):

    model.train()

    running_loss = 0.0

    for batch_index, (images, labels) in enumerate(train_loader):

        images = images.to(device)

        labels = labels.to(device)


        # Clear gradients

        optimizer.zero_grad()


        # Forward

        outputs = model(images)


        # Loss

        loss = criterion(
            outputs,
            labels
        )


        # Backpropagation

        loss.backward()


        # Update weights

        optimizer.step()


        running_loss += loss.item()


        # Progress

        if (batch_index + 1) % 200 == 0:

            print(
                f"Epoch [{epoch + 1}/{EPOCHS}] "
                f"Batch [{batch_index + 1}/{len(train_loader)}] "
                f"Loss: {loss.item():.4f}"
            )


    average_loss = (
        running_loss / len(train_loader)
    )

    print(
        f"\nEpoch {epoch + 1} completed "
        f"| Average Loss: {average_loss:.4f}\n"
    )


# ==========================================
# Evaluation
# ==========================================

print("Evaluating model...")


model.eval()

correct = 0
total = 0


with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device)

        labels = labels.to(device)


        outputs = model(images)


        _, predicted = torch.max(
            outputs,
            dim=1
        )


        total += labels.size(0)

        correct += (
            predicted == labels
        ).sum().item()


accuracy = (
    100.0 * correct / total
)


print("=" * 50)

print(
    f"Test Accuracy: {accuracy:.2f}%"
)

print("=" * 50)


# ==========================================
# Save model
# ==========================================

torch.save(
    model.state_dict(),
    "model.pth"
)


print("\nModel saved as:")

print("backend/model.pth")