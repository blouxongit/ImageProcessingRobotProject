import os
import cv2

os.system("cls")


path1 = ".\\images_neg_raw\\"
path2 = ".\\images_neg_clean\\"
folder_raw = os.listdir(path1)
count = 0


for file in folder_raw:

    img = cv2.imread(path1 + file , cv2.IMREAD_GRAYSCALE)
    img_clean = cv2.resize(img , (320 , 240))
    cv2.imwrite(path2 + str(count) + ".jpg" , img_clean)
    count +=1






