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

## Problems

一開始使用fetch_mldata，一直出現WinError 10060無法取得資料，最後只好上網搜尋別人已經下載好的
在調整降維數值也花了一段時間，雖然看不太出變化，最後決定設為50，有可能是因為降維跟訓練的演算法用的太少，所以比較不出來
