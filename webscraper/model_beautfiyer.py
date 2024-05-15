import cv2
from matplotlib import pyplot as plt
import matplotlib
import torch

import numpy as np
from scipy.interpolate import RectBivariateSpline
import logger
matplotlib.use('TkAgg') 
model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

midas = torch.hub.load("intel-isl/MiDaS", model_type)

logger.PipeLine_init("starting MIDAS BACKGROUND STUFFF....")


device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

logger.Warning("got  device set ....")


midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform


logger.PipeLine_Ok("started main processes fpor ther midas stuff./..")

logger.warning("loading image...")

img = cv2.imread('/home/nicky-blackburn/Documents/Fursona-Detector/test/610hnlw0-2L._AC_UY1000_.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

logger.PipeLine_Ok("loaded image into cv")

input_batch = transform(img).to(device)


with torch.no_grad():
    prediction = midas(input_batch)

    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()

output = prediction.cpu().numpy()

print(output)

logger.PipeLine_Ok("finished the prection")


# Apply threshold to create mask
threshold = 0.5  # Adjust threshold as needed
mask = (prediction > threshold).cpu().numpy()

# Remove background using mask
foreground = np.where(mask[..., None], img, 0)

# Display the resulting foreground image
plt.imshow(foreground)
plt.axis('off')

