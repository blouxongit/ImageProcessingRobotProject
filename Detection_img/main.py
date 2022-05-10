# import the necessary packages
from imutils.video import VideoStream
import argparse
# import imutils
import time
import cv2
import os




#on doit donner en paramètre le chemin du dossier cascade
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", type=str, help = "path to input directory containing haar cascades")
args = vars(ap.parse_args())




print("[INFO] loading haar cascades...")
detector = cv2.CascadeClassifier(args["cascade"])



#on allume la caméra (on attend 1 seconde le temps qu'elle soit fonctionnelle)
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(1)



print("Démarrage du programme ...")

while True:


	#on boucle sur le flux vidéo (on récupère les images)
	frame = vs.read()
	frame = cv2.resize(frame, (512, 384))
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# perform face detection using the appropriate haar cascade


	rect = detector.detectMultiScale( gray, scaleFactor=1.25, minNeighbors=1, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)






	for (fX, fY, fW, fH) in rect:

		cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)

		print("Sommet du rectangle : ( %s , %s ), longueur : %s, largeur : %s" %(fX,fY,fW,fH)) #abscisses, ordonnée, longueur = largeur


	cv2.imshow("Frame", frame)


	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()