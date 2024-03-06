from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
import sys

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

def predict_image(image_path):
    model = ResNet50(weights='imagenet')

    preprocessed_image = load_and_preprocess_image(image_path)

    predictions = model.predict(preprocessed_image)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    print("Predictions:")
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i + 1}: {label} ({score:.2f})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resnetRecognition.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    predict_image(image_path)


def recognize_image(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['image']

        with open('temp_image.jpg', 'wb') as f:
            f.write(uploaded_image.read())

        image_path = 'temp_image.jpg'
        predictions = predict_image(image_path)

        return HttpResponse(f"Predictions: {predictions}")
    return render(request, '')