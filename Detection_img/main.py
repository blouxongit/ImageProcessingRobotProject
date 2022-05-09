# USAGE
# python chat_detection.py --image example.jpg
#    --cascade_file cascade --cascade_item "chat"
# verifiez si votre image n'est pas trop grande pour pouvoir visionner Ã  la sortie
# SI oui vous pouvez la redimensionner dans la ligne 22
# import the necessary packages
import cv2
import numpy as np
import argparse
import time


#les arguments à rentrer pour que le programme fonctionne (l'image ou l'on fait la détection et le fichier cascade)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image")
ap.add_argument("-c", "--cascade_file", required=True,
     help="path to haarcascade file")

args = vars(ap.parse_args())


image = cv2.imread(args["image"])                     # lecture de l'image


# redimensionnement de l'image
image = cv2.resize(image,(400, 400)) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)        # Converting the image to gray
cascade = cv2.CascadeClassifier(args["cascade_file"]) # Load your cascade file


# (H, W) = image.shape[:2]
# a=int(H/100)
# b=int(W/100)


# Detecting cascade items
rectangles = cascade.detectMultiScale( gray, scaleFactor = 1.05, minNeighbors = 5, minSize=(20, 20), flags = cv2.CASCADE_SCALE_IMAGE )

for (x, y, w, h) in rectangles :        # puting rectangles around them   


    # ROI = gray[ y:y+h , fx:fx+w ]

    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
# Displaying the detection 
cv2.imshow("Resultat", image)

time.sleep(15)
# cv2.waitKey(200)

# q=0
# q = int(input('entrer 1 pour arreter: '))
# while q!=1 :
#     q = int(input('entrer 1 pour arreter: '))

# cv2.destroyAllWindows()