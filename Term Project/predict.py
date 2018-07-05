from PIL import Image
from keras.models import load_model
import os
import numpy as np
import operator

''' Change "path" if the prediction target isn't in the folder '''
path = "./Resized Face Database"

    
def predict():
    print("-----Start predicting-----")
        
    model = load_model("./model.h5")
    model.summary()

    suc = 0
    normal = 0
    fail = 0
    #input_shape=(240, 180, 3)

    for filename in os.listdir(path):
        temp = Image.open(path + '/' + filename)
        ans = int(filename[1] + filename[2])
        matrix = np.array(temp) / 255
        matrix = matrix[np.newaxis, ...]
        result = model.predict(matrix)
    
        result_dict = {}
        for i in range(len(result[0])):
            result_dict[i] = float(result[0][i])
        sorted_result_dict = sorted(result_dict.items(), key=operator.itemgetter(1), reverse=True)
    
        print("\nPredictive:", sorted_result_dict[0][0])
        print("Real:", ans)
    
        if(sorted_result_dict[0][0] == ans):
            suc += 1
        elif(sorted_result_dict[1][0] == ans or sorted_result_dict[2][0] == ans or sorted_result_dict[3][0] == ans or sorted_result_dict[4][0] == ans):
            normal += 1
        else:
            fail += 1
    
        print("\nTop 5 candidates:")
        print("No. Probability")
        count = 0
        for topf in sorted_result_dict:
            count += 1
            print(str(topf[0]).zfill(2) + "  %0.8f" % topf[1])
            if count >= 5:
                break
        

    print("\nSummary")
    print("Successful:", suc, ", Normal:", normal, ", Failed:", fail)
