## Image decryption by a single-layer neural network

**Table of contents**
---------------------
- [Training samples](#training-samples)
- [Implementation](#implementation)
- [Parameters](#parameters)
- [Weight vector 𝐰](#weight-vector-𝐰)
- [Display of images](#display-of-images)
- [Problems](#problems)
- [Learning experience](#learning-experience)

### Training samples
All data are from [**e-Learning**](http://www.elearn.ndhu.edu.tw/moodle/file.php/74252/Image_and_ImageData.zip "Image and ImageData")

### Implementation

#### Pre-requisite

- Python 3
- numpy
- PIL(or pillow)

#### Function

<img src="http://chart.googleapis.com/chart?cht=tx&chl=I%20%3D%20%5Cfrac%7BE-w_%7B1%7DK_%7B1%7D-w_%7B2%7DK_%7B2%7D%7D%7Bw_%7B3%7D%7D" style="border:none;" />

#### Steps

1. 將主要python檔案以及圖片等數據儲存好，確定好相對位置，利用PIL讀取圖像
1. 將照片轉成numpy陣列，以進行計算
1. 利用其給予的演算法進行訓練，以得出梯度權重(W)
1. 將其加密算法回推，即可以未加密前的圖像

### Parameters

- MaxIterLimit: 10
- α: 1e-7
- 𝜖: 1e-30

### Weight vector 𝐰

|  |w1|w2|w3|
|--|--|--|--|
|_Value_|0.25006898|0.65998043|0.0901495|

### Display of images

**Incrypted image**

![Encrypted image](../Assignment%201/Image_and_ImageData/Eprime.png)

**Decrypted image**

![Original image](../Assignment%201/Image_and_ImageData/origin.png)

### Problems

由於很少用python所以在找相關的package的時候會花比較多的時間，像是numpy以及pillow；對於語法方面也較花時間才能確定正確的寫法。  
α、𝜖、MaxIterLimit...需要嘗試一定次數才能大約得知，也讓我試了非常多次。

### Learning experience

因為有非常多的第一次，所以嘗試起來非常花時間，但是也讓我學會許多東西。  
例如：python基本語法、numpy和PIL用途、markdown語法以及最重要的--神經網路的基礎。  
雖然把演算法和參數的用途弄懂，就已經花費了大量的時間，但是最終做出來的成的果，我覺得還是滿意的。
