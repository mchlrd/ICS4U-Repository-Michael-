import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
import numpy as np
import sys

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    return preprocess_input(img_array)

def predict_image(image_path):
    model = InceptionV3(weights='imagenet')

    preprocessed_image = load_and_preprocess_image(image_path)

    predictions = model.predict(preprocessed_image)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    print("Predictions: ")
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i+1}: {label}, ({score:.2f})")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inceptionv3_recognition.py <image_path>")
        sys.exit()

    image_path = sys.argv[1]
    predict_image(image_path)