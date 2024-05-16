import cv2
import torch
import numpy as np
import logger

logger.PipeLine_init("Loading the midas model..")

# Load the MiDaS model
model_type = "MiDaS_small"  # Choose MiDaS model type
midas = torch.hub.load("intel-isl/MiDaS", model_type)

if torch.cuda.is_available():
    device = torch.device("cuda")
    logger.info("Midas going to run on gpu....")
else:
    device = torch.device("cpu")
    logger.info("Midas going to run on cpu....")

midas.to(device)
midas.eval()

logger.PipeLine_Ok("Midas Loaded....")



logger.warning("loading image into opencv...")
# Load the image
img = cv2.imread('/home/nicky-blackburn/Documents/Fursona-Detector/test/610hnlw0-2L._AC_UY1000_.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
logger.PipeLine_Ok("loaded image....")

# Transform the image
logger.warning("trying to transform image....")

midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    logger.info("setting the transform to dpt_transform...")
    transform = midas_transforms.dpt_transform
else:
    logger.info("setting the transform to small_transform...")
    transform = midas_transforms.small_transform
input_batch = transform(img).to(device)

logger.PipeLine_Ok("transformed image....")

logger.warning("getting predicitons...")
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
mask = (prediction > threshold).cpu().numpy()

# Create a foreground image with white background
foreground = np.full_like(img, 255)

# Copy pixels from the original image to the foreground based on the mask
foreground[mask] = img[mask]

# Check prediction range
print("Min depth:", prediction.min().item())
print("Max depth:", prediction.max().item())

# Visualize the depth map
mask = (prediction < threshold).cpu().numpy().astype(np.uint8) * 255

# Invert the mask
mask = cv2.bitwise_not(mask)

# Apply the mask to the main image
foreground = cv2.bitwise_and(img, img, mask=mask)


# Display the masked &depth map image
cv2.imshow('Masked Image', foreground)
cv2.imshow('Depth Map', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
