import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import json

# Load your pre-trained classifier model
model_path = "/home/nicky-blackburn/Documents/Fursona-Detector/fursonaclassifiyer.h5"
loaded_model = tf.keras.models.load_model(model_path)

# Load and preprocess the image you want to classify at full resolution
image_path = "/home/nicky-blackburn/Documents/Fursona-Detector/test/20230205_142354.jpg"
full_res_img = cv2.imread(image_path)
full_res_img = cv2.cvtColor(full_res_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Load class labels from JSON file
json_path = 'class_names.json'
with open(json_path, 'r') as json_file:
    class_labels = json.load(json_file)

# Resize and preprocess the image for model input
img_array = cv2.resize(full_res_img, (150, 150))  # Resize to model input size
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalize pixel values to [0, 1]

# Prediction threshold
threshold = 0.5

# Make predictions
predictions = loaded_model.predict(img_array)

# Loop through each class label
for i, prediction in enumerate(predictions[0]):
    if prediction > threshold:
        predicted_class = i
        predicted_class_name = class_labels[str(predicted_class)]
        probability = prediction

        print(f"Predicted Class: {predicted_class}")
        print(f"Probability: {probability}")
        print(f"Predicted Class Name: {predicted_class_name}")

        # Draw bounding box and class label on the full-resolution image
        cv2.putText(full_res_img, f"Class: {predicted_class_name}", (10, 30 + i * 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(full_res_img, f"Acc: {probability:.2f}", (10, 60 + i * 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Display the image with bounding boxes
cv2.imshow("Full Resolution Image with Predictions", full_res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
