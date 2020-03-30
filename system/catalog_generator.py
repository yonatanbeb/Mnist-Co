from keras.datasets import fashion_mnist
from PIL import Image

(images, _), (_, _) = fashion_mnist.load_data()
images = images[:100]

generate = False
if generate:
    for i in range(100):
        image = Image.fromarray(images[i])
        image.save('catalog/' + str(i) + '.png')

