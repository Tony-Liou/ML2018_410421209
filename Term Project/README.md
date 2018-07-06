# Face Recognition

**_Table of contents_**
---------------------
- [Machine learning technology](#machine-learning-technology)
- [Modules and functions](#modules-and-functions)
- [Testing recognition rate](#testing-recognition-rate)
- [Problems](#problems)
- [Experience and feeling](#experience-and-feeling)
- [Resource](#resource)

## Machine learning technology

使用三層卷積神經網絡(Convolutional Neural Network)來訓練資料，優化器採用Adam。

## Modules and functions

程式分為三個主要部分:
1. 圖像預處理
1. 訓練
1. 預測

### 圖像預處理

將要訓練的圖片轉換成同樣大小以方便後續操作

### 訓練

利用*Keras(Tensorflow)* 可以快速又方便的完成訓練，利用卷積層、dropout等等來計算、池化或防止過擬合(overfitting)，最後得出模型

### 預測

載入訓練後的模型，直接使用內建method(predict)直接進行測試，顯示最有可能的五名人選，並顯示機率

最後統計直接命中(`successful`)、間接命中(`normal`)或是未命中(`failed`)

## Testing recognition rate

每個人15張頭像中，隨機抽取1到2張圖片不做訓練，在預測階段做為測試資料來看成功辨識的機率

## Problems

因為這次沒有給演算法的方向，因此在上網找資料的部分花了大部分的時間。
而*Keras*和*Tensorflow*的安裝也蠻複雜的，最後才發現全部裝在*Anaconda*上面最簡單......

在測試中，一開始的辨識率蠻低的，後來才發現用的神經網絡太少了，因此又多補了一些上去

`epoch`、`batch_size`等參數也是在寫程式的時候調整了很多次，再拿到測資時也修正了一些，最後的辨識率才能達到九成以上

## Bonus features or functionalities

:x:

## Experience and feeling

雖然機器學習導論的這門課一點也不導論，正因如此，也讓我學到許多實作技巧與知識。

像以前聽到Alpha Go的演算法就覺得高深莫測，一輩子都不可能學會，但是經過這次的卷積神經網絡的練習後，覺得開始能夠看的到一些基礎的機器學習演算法，實在是感到非常的興奮和充實。

希望將來有機會還能夠接觸到更多有趣、好玩或實用的程式或演算法，讓我的電腦科學的知識更上層樓。

## Resource

- [Face Database](http://www.elearn.ndhu.edu.tw/moodle/mod/resource/view.php?id=368737)
- [Specifications of the Face Recognizer System for ML Term Project](http://www.elearn.ndhu.edu.tw/moodle/file.php/74252/Specifications_of_the_Face_Recognizer_System_for_ML_Term_Project.pdf)
