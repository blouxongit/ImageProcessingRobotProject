import cv2
# entrer le nom du fichier de l'image
filename = "cible.jpg"  
#lire l'image
oriimg = cv2.imread(filename) 
# redimensionnement de l'image
newimg = cv2.resize(oriimg,(100, 100))  
# afficher l'image
cv2.imshow("Show by CV2",newimg)
cv2.waitKey(0)
# sauvegarder l'image
cv2.imwrite("positive.jpg",newimg)