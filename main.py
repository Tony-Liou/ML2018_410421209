from PIL import Image
import numpy as np
import os

E = Image.open('C:\\Users\\Tony\\Documents\\GitHub\\ML2018_410421209\\Image_and_ImageData\\E.png')
key1 = Image.open('C:\\Users\\Tony\\Documents\\GitHub\\ML2018_410421209\\Image_and_ImageData\\key1.png')
key2 = Image.open('C:\\Users\\Tony\\Documents\\GitHub\\ML2018_410421209\\Image_and_ImageData\\key2.png')
I = Image.open('C:\\Users\\Tony\\Documents\\GitHub\\ML2018_410421209\\Image_and_ImageData\\I.png')
Eprime = Image.open('C:\\Users\\Tony\\Documents\\GitHub\\ML2018_410421209\\Image_and_ImageData\\Eprime.png')
# img.show()
E.show()
key1.show()
key2.show()
I.show()
Eprime.show()

width, height = E.size

print(width,height)
os.system("pause")
