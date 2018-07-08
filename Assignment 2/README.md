# Handwritten digit recognition

## Implementation

1. 從網路擷取數據
1. 數值標準化
1. 降低維度
1. 分類
1. 測試辨識準確度

## Functions

使用scikit-learn作為主要的package
- fetch_mldata
- train_test_split
- PCA(Principal Component Analysis)
- SVC(Support Vector Machine)

## SVM Report

Label | Precision | recall | f1-score | support
--- | --- | --- | --- | ---
0 | 0.99 | 0.99 | 0.99 | 727
1 | 0.99 | 0.98 | 0.98 | 741
2 | 0.98 | 0.98 | 0.98 | 732
3 | 0.98 | 0.97 | 0.98 | 689
4 | 0.97 | 0.99 | 0.98 | 727
5 | 0.98 | 0.99 | 0.98 | 618
6 | 0.99 | 0.99 | 0.99 | 693
7 | 0.98 | 0.99 | 0.98 | 752
8 | 0.97 | 0.97 | 0.97 | 642
9 | 0.98 | 0.97 | 0.97 | 679
avg / total | 0.98 | 0.98 | 0.98 | 7000


## Problems

一開始使用fetch_mldata，一直出現WinError 10060無法取得資料，最後只好上網搜尋別人已經下載好的
在調整降維數值也花了一段時間，雖然看不太出變化，最後決定設為50，有可能是因為降維跟訓練的演算法用的太少，所以比較不出來
