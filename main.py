from PIL import Image
import numpy as np
import random
import os

# Read images
E = Image.open("Image_and_ImageData/E.png")
key1 = Image.open("Image_and_ImageData/key1.png")
key2 = Image.open("Image_and_ImageData/key2.png")
I = Image.open("Image_and_ImageData/I.png")
Eprime = Image.open("Image_and_ImageData/Eprime.png")
#I.show()
width, height = E.size
#print(width,height)
output = Image.new("L",(width, height), 0)


os.system("pause")

w1 = np.random.rand(1)
w2 = np.random.rand(1)
w3 = np.random.rand(1)

# Convert image to numpy's array
arrK1 = np.array(key1)
arrK2 = np.array(key2)
arrI = np.array(I)
arrE = np.array(E)
arrEP = np.array(Eprime)

# Setting parameter of gradient descent"""
rate = 1e-7
#epoch = 69
epoch = 1
limit = 10 # MaxIterLimit

a = np.zeros((width, height))
e = np.zeros((width, height))

while(epoch == 1 or epoch < limit):
    for w in range(0, width - 1):
        for h in range(0, height - 1):
            a[w,h] = (arrK1[w,h] * w1) + (arrK2[w,h] * w2) + (arrI[w,h] * w3)
            e[w,h] = arrE[w,h] - a[w,h]
            w1 += rate * e[w,h] * arrK1[w,h]
            w2 += rate * e[w,h] * arrK2[w,h]
            w3 += rate * e[w,h] * arrI[w,h]
    print("epoch: ", epoch)
    print("weight: ", w1, w2, w3)
    epoch += 1

new = np.zeros((width, height))
new = (EP-(w1*k1)-(w2*k2))/w3

new = Image.fromarray(new)
new = new.convert('RGB')
new.save("Iprime.jpg")
new.show()
