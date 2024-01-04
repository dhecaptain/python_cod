import cv2
import numpy as np
import imageio
import scipy.ndimage

img_path = "IMG_1694894995982.jpg"

def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

def dodge(front, back):
    result = front * 255 / (np.clip(255 - back, a_min=1, a_max=None))
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')

# Read the image using imageio
s = imageio.imread(img_path)

# Convert the image to grayscale
g = grayscale(s)

# Invert the grayscale image
i = 255 - g

# Apply Gaussian filter
b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)

# Create the final sketch
c = dodge(b, g)

# Display the original image
cv2.imshow("Original Image", s)

# Display the sketch
cv2.imshow("Sketch", c)

# Wait for a key event and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
