import unisize
import training
import predict

#ori_path = "./Face Database" # original
#res_path = "./Resized Face Database" # resized

unisize.uni_size() # Ask if need to resize the images
training.train()
predict.predict()
