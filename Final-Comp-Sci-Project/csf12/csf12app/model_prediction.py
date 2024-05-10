import os
import cv2 as cv
import numpy as np
import tensorflow as tf
from csf12.settings import BASE_DIR


def digit_prediction(img):
    model = tf.keras.models.load_model(os.path.join(BASE_DIR, "csf12app\handwritten_model.keras"))

    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    img_inverted = cv.bitwise_not(img_gray)
    img_resized = cv.resize(img_inverted, (28, 28))
    img_reshaped = img_resized.reshape((1, 28, 28))

    prediction = np.argmax(model.predict(img_reshaped))
    return prediction