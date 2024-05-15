import cv2
import torch
import mediapipe as mp
import numpy as np
from scipy.interpolate import RectBivariateSpline

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False)

#Downloading the model from TorchHub.
midas = torch.hub.load('intel-isl/MiDaS','MiDaS_small')
midas.to('cpu')
midas.eval()