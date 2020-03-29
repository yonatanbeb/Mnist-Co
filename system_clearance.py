import os
import numpy as np
from random import randrange
from PIL import Image
from keras.datasets import mnist
from keras.models import load_model
import keras.backend as K


MODEL_PATH = os.path.abspath('../system_data/models')

labels = {
    # Clearance Level 1 Labels
    0: 'T-Shirt',
    1: 'Trouser',
    2: 'Pullover',
    3: 'Dress',
    4: 'Coat',
    5: 'Sandal',
    6: 'Shirt',
    7: 'Sneaker',
    8: 'Bag',
    9: 'Boot',
    # Clearance Level 0 Labels
    10: 'Top',
    11: 'Bottom',
    12: 'Shoe',
    # No Clearance Level Label
    13: 'No Clearance'
}

########################################################################################################################

(digit_images, digit_labels), (_, _) = mnist.load_data()
zeros, ones = [], []

for i in range(len(digit_images)):
    if digit_labels[i] == 0:
        zeros.append(digit_images[i])
    elif digit_labels[i] == 1:
        ones.append(digit_images[i])

zeros = np.asarray(zeros, dtype=np.uint8)
len0 = len(zeros)
ones = np.asarray(ones, dtype=np.uint8)
len1 = len(ones)


########################################################################################################################

def encode(image, clearance_level):
    if clearance_level == 0:
        return image + zeros[randrange[len0]]
    return image + ones[randrange(len1)]


########################################################################################################################

def auto_encode(image, clearance_level):
    if clearance_level == 'No Clearance':
        return image

    Encoder = load_model(MODEL_PATH + '/encoder_' + str(clearance_level) + '.h5')
    Decoder = load_model(MODEL_PATH + '/decoder_' + str(clearance_level) + '.h5')

    encoded_image = encode(image, clearance_level)
    encoded_image = (encoded_image.astype('float32') / 255).reshape(1, 784)

    encoded_image = Encoder.predict(encoded_image, verbose=1)
    auto_encoded_image = Decoder.predict(encoded_image, verbose=1)

    auto_encoded_image = (auto_encoded_image * 255).astype('uint8').reshape(28, 28)

    return auto_encoded_image


########################################################################################################################

def predict(image):
    Model = load_model(MODEL_PATH + '/classifier.h5')
    if K.image_data_format() == 'channels_first':
        image = image.reshape(1, 1, 28, 28)
    else:
        image = image.reshape(1, 28, 28, 1)
    image = image.astype('float32') / 255

    return labels[int(np.argmax(Model.predict(image, verbose=1)))]


########################################################################################################################

