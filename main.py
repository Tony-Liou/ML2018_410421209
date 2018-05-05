from PIL import Image
import numpy as np

# Read images
E = Image.open("Image_and_ImageData/E.png")
key1 = Image.open("Image_and_ImageData/key1.png")
key2 = Image.open("Image_and_ImageData/key2.png")
I = Image.open("Image_and_ImageData/I.png")
Eprime = Image.open("Image_and_ImageData/Eprime.png")

# Get the size of the images
width, height = E.size
output = Image.new("L", (width, height), 0)

# Convert images to numpy array
arrE = np.array(E)
arrK1 = np.array(key1)
arrK2 = np.array(key2)
arrI = np.array(I)

# Setting the parameters
w = np.zeros(3) # [0., 0., 0.] randomize
max = 10 # Max iteration limit
epsilon = 1e-30 # vigilance level
alpha = 1e-7 # Learning rate
epoch = 1 # time(s)

# Training algorithm
while True:
    preW = w
    for i in range(0, height-1):
        for j in range(0, width-1):
            x = np.array([arrK1[i][j], arrK2[i][j], arrI[i][j]])
            a = w.dot(x.T) # dot is matrix multiplication, T is transpose
            e = arrE[i][j] - a
            w = w + (alpha * e) * x

    if epoch >= max or abs(np.linalg.norm(w - preW)) <= epsilon:
        break
    epoch += 1

output = (Eprime - (w[0] * key1) - (w[1] * key2)) / w[2] # '*' is also matrix multiplication
Image.fromarray(output).show() # Display the final image
