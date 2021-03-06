# import the necessary packages
from imutils.video import VideoStream
import argparse
# import imutils
import time
import cv2
import os
from math import exp,log


#fonction pour envoyer la commande de déplacement

FRAME_SIZE_WIDTH = 512

def commandeMove(x,w):

	ordreMove = 3

	if int(x+w/2) > int( FRAME_SIZE_WIDTH/2 + 6):
		return( -ordreMove )
		

	if int(x+w/2) < int( FRAME_SIZE_WIDTH/2 - 6):
		return( ordreMove )

	print("Cible face à la caméra")

	



#fonction pour raph
data = []
def getData():
	#print(data)
	return(data)



#on doit donner en paramètre le chemin du dossier cascade (le défaut est pour windows)
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", type=str, help = "path to input directory containing haar cascades", default="data_v2\cascade.xml")
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


	#on detecte la cible
	rect = detector.detectMultiScale( gray, scaleFactor=1.25, minNeighbors=1, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)






	for (i, (fX, fY, fW, fH)) in enumerate(rect):



		data = [fX,fW]
		getData()
		where = commandeMove(fX,fW)
		print(where)

		cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)

		# print("Sommet du rectangle : ( %s , %s ), longueur : %s, largeur : %s" %(fX,fY,fW,fH)) #abscisses, ordonnée, longueur = largeur

		#approche puissance
		distance = int(13315*exp(-0.986*log(fH)))

		

		#approche polynomiale
		#a = [ 582.25 , -9.7464 , 0.0843, -4e-4 , 9e-7 , -8e-10 ]
		#distance = a[0]*fH**0 + a[1]*fH + a[2]*fH**2 + a[3]*fH**3 + a[4]*fH**4 - a[5]*fH**5 


		if 40 < distance < 250:

			print(f"\rDistance à la cible n°{i+1} : {distance}cm")	



	cv2.imshow("Frame", frame)
	

	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
	

 #on ferme la fenetre et on arrete la webcam
cv2.destroyAllWindows()
vs.stop()