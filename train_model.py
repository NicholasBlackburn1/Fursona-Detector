
# pro tip keep model res 150 x 150 and mabey save it
import os 
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import TensorBoard
from datetime import datetime


# Set up Tensor
log_dir = "logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

# saves classifications to the file 
dataset_path = '/home/nicky-blackburn/Documents/Fursona-Detector/webscraper/dataset'
class_labels = sorted(os.listdir(dataset_path))
num_classes = len(class_labels)
print("Class Labels:", class_labels)

# Write class names to JSON file
json_path = 'class_names.json'
with open(json_path, 'w') as json_file:
    json.dump(class_labels, json_file)
print(f"Class names written to {json_path}")



# Load Dataset
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    '/home/nicky-blackburn/Documents/Fursona-Detector/webscraper/dataset',
    target_size=(150, 150),
    batch_size=38,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    '/home/nicky-blackburn/Documents/Fursona-Detector/webscraper/dataset',
    target_size=(150, 150),
    batch_size=38,
    class_mode='categorical',
    subset='validation'
)

# Build Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(train_generator.num_classes, activation='softmax')
])

# Compile Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Configure TensorBoard callback
tensorboard_callback = TensorBoard(log_dir='./logs', histogram_freq=1, write_graph=True, write_images=True)

# Train Model with TensorBoard callback
history = model.fit(
    train_generator,
    epochs=45,
    validation_data=validation_generator,
    callbacks=[tensorboard_callback]
)

# Save Model
model.save('fursonaclassifiyer.keras')