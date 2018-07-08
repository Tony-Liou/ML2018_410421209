from sklearn.datasets import fetch_mldata
'''import numpy as np
import matplotlib.pyplot as plt #plotting package'''
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

import time

# Setting PCA dimension value after reducing dimension
COMPONENT_NUM = 50
DATA_PATH = '~/scikit_learn_data'

print("Fetch training data...")
mnist = fetch_mldata('MNIST original', data_home=DATA_PATH) # https://github.com/amplab/datascience-sp14/blob/master/lab7/mldata/mnist-original.mat
print("Fetch finished")

'''
img = np.reshape(mnist.data[0,:], (28,28)) # reshape 1-D vector of the first example to a 2-D image, first row of the array
plt.imshow(img, cmap=plt.cm.gray ) # prepare image for display
plt.show() # display image
'''

mnist.data = mnist.data / 255 # Normalize

pca = PCA(n_components=COMPONENT_NUM, whiten=True)
# Fit the model with X
pca.fit(mnist.data)
# Reducing dimension
X = pca.transform(mnist.data)
Y = mnist.target

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1)

svc = SVC()
tStart = time.clock() # Timer start
svc.fit(x_train, y_train)
tEnd = time.clock() # Timer stop
print("Training costs:", tEnd - tStart, "sec")

tStart = time.clock()
predict = svc.predict(x_test)
tEnd = time.clock()
print("Predicting costs:", tEnd - tStart, "sec")

print("Classification report for classifier SVM:\n%s\n"
      % (metrics.classification_report(y_test, predict)))

cm = metrics.confusion_matrix(y_test, predict)
print("Confusion matrix:\n%s\n" % cm)


right = 0
wrong = 0
for i in range(len(predict)):
    if y_test[i] == predict[i]:
        right += 1
    else:
        wrong += 1

print("Right:", right, ", wrong:", wrong)
print("Classsifier accuracy: %.5f" % metrics.accuracy_score(y_test, predict))