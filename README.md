# Image Steganography using LSB and XOR Operation on MSB
A dirty implementation of the research paper "Simple and Secure Image Steganography using LSB and Triple XOR Operation on MSB" published by Yani et al (https://ieeexplore.ieee.org/document/8350661/)

embedding.py
```
usage: embedding.py [-h] -c COVER_IMAGE -m MESSAGE_IMAGE -s STEGO_IMAGE

optional arguments:
  -h, --help            show this help message and exit
  -c COVER_IMAGE, --cover_image COVER_IMAGE
                        path to cover image
  -m MESSAGE_IMAGE, --message_image MESSAGE_IMAGE
                        path to message image
  -s STEGO_IMAGE, --stego_image STEGO_IMAGE
                        path to save stego image
```


extraction.py
```
usage: extraction.py [-h] -s STEGO_IMAGE -r RECOVER_IMAGE

optional arguments:
  -h, --help            show this help message and exit
  -s STEGO_IMAGE, --stego_image STEGO_IMAGE
                        path to stego image
  -r RECOVER_IMAGE, --recover_image RECOVER_IMAGE
                        path to save recovered image
```                        

Refer to Jupyter Notebook for more details.
