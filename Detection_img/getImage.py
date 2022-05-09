import cv2
import numpy
import matplotlib.image as mp


def getImage():

    # Acces a la camera
    cam = cv2.VideoCapture(0)

    count = 0
    while count < 30:
        ret, image = cam.read()
        if cv2.waitKey(50) &0xFF == ord('q'):
            break
        copy_image = numpy.copy(image)
        image_name = 'testIMG/image_test' + str(count) + '.png'
        mp.imsave(image_name, copy_image)
        count += 1
        print(count)




getImage()