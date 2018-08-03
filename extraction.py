# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 00:10:15 2018

@author: YQ
"""

import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--stego_image", required=True,
                help="path to stego image")
ap.add_argument("-r", "--recover_image", required=True,
                help="path to save recovered image")
args = vars(ap.parse_args())

# step 1: read stego image
stego_img = cv2.imread(args["stego_image"], 0)

# step 2: change pixel value to binary
stego_flatten = stego_img.flatten()
#stego_flatten = [np.binary_repr(x, width=8) for x in stego_flatten]

out = []
for x in stego_flatten:
    x = np.binary_repr(x, width=8)

    # step 3: perform XOR on 7th and 6th bits
    xor_a = int(x[1]) ^ int(x[2])
    
    # step 4: perform XOR operation on 8th bit with xor_a
    xor_b = int(x[0]) ^ xor_a
    
    # step 5: perform XOR operations on message bits with 3 MSB
    xor_c = int(x[-1]) ^ xor_b
    
    out.append(int(xor_c))
    
recover_img = np.reshape(np.array(out), (256,256))
recover_img[recover_img==1] = 255
cv2.imwrite(args["recover_image"], recover_img)