import cv2
import torch
import numpy as np
import logger

logger.PipeLine_init("Loading the midas model..")

# Load the MiDaS model
model_type = "DPT_Large"  # Choose MiDaS model type
midas = torch.hub.load("intel-isl/MiDaS", model_type)

if torch.cuda.is_available():
    device = torch.device("cuda")
    logger.warning("Midas going to run on gpu....")
else:
    device = torch.device("cpu")
    logger.warning("Midas going to run on cpu....")
    
midas.to(device)
midas.eval()

logger.PipeLine_Ok("Midas Loaded....")

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
        mode="bilinear",  # Change interpolation method to bilinear
        align_corners=False,
    ).squeeze()

# Apply threshold to create mask
threshold = 1.0  # Adjust threshold as needed
mask = (prediction).cpu().numpy()

# Create a foreground image with white background
foreground = np.full_like(img, 255)

# Copy pixels from the original image to the foreground based on the mask
foreground[mask] = img[mask]

# Display the foreground
cv2.imshow('Foreground', cv2.cvtColor(foreground, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
