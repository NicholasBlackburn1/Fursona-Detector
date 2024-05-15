import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

# Load your pre-trained classifier model
model_path = "/home/nicky-blackburn/Documents/Fursona-Detector/fursonaclassifiyer.h5"
loaded_model = tf.keras.models.load_model(model_path)

# Load and preprocess the image you want to classify at full resolution
image_path = "/home/nicky-blackburn/Documents/Fursona-Detector/test/20230205_142354.jpg"
full_res_img = cv2.imread(image_path)
full_res_img = cv2.cvtColor(full_res_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
img_array = cv2.resize(full_res_img, (150, 150))  # Resize to model input size
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalize pixel values to [0, 1]

# Define your class labels
class_labels = ["bovine", "canine", "cervine", "hybrid", "mustelid", "mythical", "scalie"]

#the thresh of too keep the ml at bey 
threshold = 0.5

# Loop through each class label
for class_label in class_labels:
    # Make predictions
    predictions = loaded_model.predict(img_array)

    # Get the class with the highest probability
    predicted_class = np.argmax(predictions[0]-1)

    # Check if the prediction probability is less than 0.62
    if (predictions[0][predicted_class]-1 > threshold): 
        # Print the predicted class and probability
        print(f"Predicted Class: {predicted_class}")
        print(f"Probability: {predictions[0][predicted_class]}")

        proba = predictions[0][predicted_class]

        # Print the corresponding class name
        predicted_class_name = class_labels[predicted_class]
        print(f"Predicted Class Name: {predicted_class_name}")

        # Draw bounding box on the full-resolution image
        cv2.putText(full_res_img, f"Class: {predicted_class_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(full_res_img, f"Acc:{predictions[0][predicted_class]}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the image with bounding boxes
        cv2.imshow("Full Resolution Image with Prediction", full_res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("im sorry but doesnt meet my qauilty standereds.... What Standereds im A Furry~")
