import os
import numpy as np
from random import randrange
from keras.datasets import mnist
from keras.models import load_model
import keras.backend as K

########################################################################################################################

MODEL_PATH = os.path.abspath('./system/models')

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
""" retrieve 0s and 1s from mnist to encode fashion_mnist """

# unload mnist
(digit_images, digit_labels), (_, _) = mnist.load_data()
zeros, ones = [], []

for i in range(len(digit_images)):
    if digit_labels[i] == 0:
        zeros.append(digit_images[i])
    elif digit_labels[i] == 1:
        ones.append(digit_images[i])

# numpy array of all 0s in mnist
zeros = np.asarray(zeros, dtype=np.uint8)
len0 = len(zeros)
# numpy array of all 1s in mnist
ones = np.asarray(ones, dtype=np.uint8)
len1 = len(ones)


########################################################################################################################
""" system image encoding mechanism """


def encode(image, clearance_level):
    """
    INPUT:
        image - numpy array of fashion_mnist image (from catalog)
        clearance_level - level to encode image with (from surfer)
    OUTPUT:
        returns image encoded with clearance level ==> image + mnist digit image
    """
    if clearance_level == 0:
        # generate random 0 to encode image
        return image + zeros[randrange(len0)]
    # generate random 1 to encode image
    return image + ones[randrange(len1)]


def auto_encode(image, clearance_level):
    """
    INPUT:
        image - numpy array of fashion_mnist image (from catalog)
        clearance_level - level to encode image with (from surfer)
    OUTPUT:
        returns image auto encoded with clearance level
    """
    # if surfer is guest -- image doesn't get encoded
    if clearance_level == 'No Clearance':
        return image

    # load clearance level models
    Encoder = load_model(MODEL_PATH + '/encoder_' + str(clearance_level) + '.h5')
    Decoder = load_model(MODEL_PATH + '/decoder_' + str(clearance_level) + '.h5')

    # encode image
    encoded_image = encode(image, clearance_level)
    # normalize and reshape image
    encoded_image = (encoded_image.astype('float32') / 255).reshape(1, 784)

    # auto encode image
    encoded_image = Encoder.predict(encoded_image, verbose=1)
    auto_encoded_image = Decoder.predict(encoded_image, verbose=1)

    return (auto_encoded_image * 255).astype('uint8').reshape(28, 28)


########################################################################################################################
""" system image prediction mechanism """


def predict(image):
    """
    INPUT:
        image - numpy array of fashion_mnist image (from catalog)
    OUTPUT:
        returns the label of image according to surfers clearance_level
    """
    # load classifier model
    Model = load_model(MODEL_PATH + '/classifier.h5')
    # reshape image
    if K.image_data_format() == 'channels_first':
        image = image.reshape(1, 1, 28, 28)
    else:
        image = image.reshape(1, 28, 28, 1)
    # normalize image
    image = image.astype('float32') / 255

    # predict image
    return labels[int(np.argmax(Model.predict(image, verbose=1)))]


########################################################################################################################

