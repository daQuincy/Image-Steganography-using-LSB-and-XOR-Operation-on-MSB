# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 22:37:23 2018

@author: YQ
"""

import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cover_image", required=True,
                help="path to cover image")
ap.add_argument("-m", "--message_image", required=True,
                help="path to message image")
ap.add_argument("-s", "--stego_image", required=True,
                help="path to save stego image")
args = vars(ap.parse_args())

# step 1: read the cover image and message image
c_img = cv2.imread(args["cover_image"], 0)
c_img = cv2.resize(c_img, (256, 256))

m_img = cv2.imread(args["message_image"], 0)
m_img = cv2.resize(m_img, (256, 256))
m_img[m_img>0] = 1


# step 2: change the pixel value to binary
c_flatten = c_img.flatten()
#c_flatten = [np.binary_repr(x, width=8) for x in c_flatten]

m_flatten = np.reshape(m_img, (-1,))

# https://stackoverflow.com/questions/1523465/binary-numbers-in-python
out = []
for a, b in zip(c_flatten, m_flatten):
    a = np.binary_repr(a, width=8)

    # step 3: perform XOR operations on the 7th and on the 6th bit    
    xor_a = int(a[1]) ^ int(a[2])
    
    # step 4: perform XOR operations on 8th bit with xor_a
    xor_b = int(a[0]) ^ xor_a
    
    # step 5: perform XOR operations on message bits with 3 MSB
    xor_c = int(b) ^ xor_b 
    
    # step 6: save xor_c, convert back to uint8
    save = a[:-1] + str(xor_c)
    
    # https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int
    out.append(int(save, 2))
    
stego_img = np.array(out)
stego_img = np.reshape(stego_img, (256, 256))

cv2.imwrite(args["stego_image"], stego_img)
    