import cv2
import torch
import numpy as np

# Load the MiDaS model
model_type = "DPT_Large"  # Choose MiDaS model type
midas = torch.hub.load("intel-isl/MiDaS", model_type)
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

# Load the image
img = cv2.imread('/home/nicky-blackburn/Documents/Fursona-Detector/test/610hnlw0-2L._AC_UY1000_.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Transform the image
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform
input_batch = transform(img).to(device)

# Get the prediction from MiDaS
with torch.no_grad():
    prediction = midas(input_batch)
    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()

# Apply threshold to create mask
threshold = 1.0  # Adjust threshold as needed
mask = (prediction > threshold).cpu().numpy()

# Remove background using the mask
foreground = img.copy()
foreground[~mask] = 6  # Set non-masked pixels to white (255)

# Display the foreground
cv2.imshow('Foreground', cv2.cvtColor(foreground, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()