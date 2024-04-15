# -*- coding: utf-8 -*-
"""
RGB-recombination
Turn a color palette into another
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# load image
img = cv.imread('testImg.PNG') 
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) # this is necessay as opencv uses GBR rather than RGB--have to swap the channels otherwise matplotlib doesn't plot correctly
plt.imshow(img)
plt.title('original image')
plt.show()

# decompose into RGB channel
r,g,b = cv.split(img)

fig, axs = plt.subplots(nrows=3, sharex=True, figsize=(5, 8))

axs[0].imshow(b,cmap='gray')
axs[0].set_title('blue channel')

axs[1].imshow(g,cmap='gray')
axs[1].set_title('green channel')

axs[2].imshow(r, cmap='gray')
axs[2].set_title('red channel')
plt.show()

## now lets do image recombination
# now lets throw away the blue channel and recreate it via a combination of red and green
# This is the typical way to achieve "hubble like" colors i.e. blue and gold from a one-shot color camera 
# The final colors will depend on the original image i.e. more gold/blue 
blue = ((0.6*r)+(0.4*g)).astype(np.uint8)

# now lets plot and compare the increase in SNR-again we dont care about color
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(5, 8))
axs[0].set_title('original blue channel')
axs[0].imshow(b, cmap='gray')

axs[1].set_title('new blue channel')
axs[1].imshow(blue, cmap='gray')
plt.show()

# now lets recombine all the channels and see
hubble = cv.merge([r,blue,g]) # swap the blue and green channels are blue re-combination
plt.imshow(hubble)
plt.title('New image (hubble-palette)')
plt.show()

#Now you can accentuate the gold and blue in photoshop, or some other software, using masks and curve adjsutments to end up with something like this:
fin = cv.imread('completed.PNG') 
fin = cv.cvtColor(fin, cv.COLOR_BGR2RGB) # this is necessay as opencv uses GBR rather than RGB--have to swap the channels otherwise matplotlib doesn't plot correctly


fig, axs = plt.subplots(nrows=2, figsize=(5, 8))
axs[0].set_title('original image')
axs[0].imshow(img)

axs[1].set_title('completed image')
axs[1].imshow(fin)
plt.show()

# save the image
# remember to convert back to BGR since OpenCV uses BGR and not RGB
cv.imwrite('hubblePalette.PNG', cv.cvtColor(hubble, cv.COLOR_RGB2BGR)) 