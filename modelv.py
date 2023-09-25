import torch
from torchvision import models


model_path = "weights/0826_detect_landmark.pt"  # Specify the correct path to your model file

# Load the model
model = torch.load(model_path, map_location=torch.device('cuda'))

# Print the PyTorch version
print("PyTorch version:", torch.__version__)