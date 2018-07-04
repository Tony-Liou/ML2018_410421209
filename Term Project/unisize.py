import os
from PIL import Image

ori_path = "./Face Database" # original
res_path = "./Resized Face Database" # resized

def existed():

    if os.path.exists(res_path):
        print("The folder has already existed.")
        ans = input("Resize?[y/n]")
        if ans == "y":
            return False
        else:
            return True
    else:
        os.makedirs(res_path)
        return False

def uni_size():

    if existed():
        return

    for filename in os.listdir(ori_path):
        new_img = Image.open(ori_path + '/' + filename)
        new_img = new_img.resize((180, 240), Image.BILINEAR) # 雙線性
        new_img.save(res_path + '/' + filename)

    print("Images unified")
