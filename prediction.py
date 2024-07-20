
import os

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import tensorflow_hub as hub
import numpy as np


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(ROOT_PATH, 'models')
model_path = os.path.join(model_dir, "efficientnet_b0_shoes_classifier.h5")

class_labels = ['boots', 'flip_flops', 'loafers', 'sandals', 'sneakers', 'soccer_shoes']
model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer': hub.KerasLayer}) 

# Function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Create batch axis
    img_array /= 255.0  # Normalize the image
    return img_array


# Function to make predictions
def predict_image(img_path):
    preprocessed_image = preprocess_image(img_path)
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions, axis=1)
    predicted_label = class_labels[predicted_class[0]]
    return predicted_label, predictions[0]


if __name__ == "__main__":
    # Load the saved model
    images_path = os.path.join(ROOT_PATH, "test_images")
    test_image = os.path.join(images_path, "test_image2.jpg")
    
    predicted_label, prediction_scores = predict_image(test_image)
    print(predicted_label)