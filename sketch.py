import cv2 
import numpy as np
import imageio.v2 as imageio
import scipy.ndimage
img="WIN_20240101_19_10_51_Pro.jpg"#IMG_1694894995982.jpg

def grayscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back):
    result=front *255/(np.clip(255-back, a_min=1, a_max=None))
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

s=imageio.imread(img)
g=grayscale(s)
i=255-g

b=scipy.ndimage.filters.gaussian_filter(i,sigma=10)
c=dodge(b,g)