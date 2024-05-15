import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import json

# Load your pre-trained classifier model
model_path = "/home/nicky-blackburn/Documents/Fursona-Detector/fursonaclassifiyer.h5"
loaded_model = tf.keras.models.load_model(model_path)

# Load and preprocess the image you want to classify at full resolution
image_path = "/home/nicky-blackburn/Documents/Fursona-Detector/test/61dLWeIGm9L._AC_UY1000_.jpg"
full_res_img = cv2.imread(image_path)
full_res_img = cv2.cvtColor(full_res_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
img_array = cv2.resize(full_res_img, (150, 150))  # Resize to model input size
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalize pixel values to [0, 1]

# Load class labels from JSON file
json_path = 'class_names.json'
with open(json_path, 'r') as json_file:
    class_labels = json.load(json_file)

# The threshold to keep the prediction
threshold = 0.5

# Loop through each class label
for class_label in class_labels:
    # Make predictions
    predictions = loaded_model.predict(img_array)

    # Get the class with the highest probability
    predicted_class = np.argmax(predictions[0])

    # Check if the prediction probability is less than the threshold
    if predictions[0][predicted_class] > threshold:
        # Print the predicted class and probability
        print(f"Predicted Class: {predicted_class}")
        print(f"Probability: {predictions[0][predicted_class]}")

        proba = predictions[0][predicted_class]

        # Print the corresponding class name
        predicted_class_name = class_labels[predicted_class]
        print(f"Predicted Class Name: {predicted_class_name}")
        
    else:
        print("I'm sorry but it doesn't meet my quality standards... What standards? I'm a Furry~")