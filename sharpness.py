from PIL import Image
import numpy as np

image_file = 'images/combi-sharp.jpg'

im = Image.open(image_file).convert('L') # to grayscale
array = np.asarray(im, dtype=np.int32)

gy, gx = np.gradient(array)
gnorm = np.sqrt(gx**2 + gy**2)
sharpness = np.average(gnorm)

print(f'Sharpness: {sharpness:.4f}')

#image_file = 'images/combi-10-blur.jpg'
# Sharpness: 1.4933