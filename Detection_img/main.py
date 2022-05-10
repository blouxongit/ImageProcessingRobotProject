# import the necessary packages
from imutils.video import VideoStream
import argparse
# import imutils
import time
import cv2
import os





# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", type=str, help = "path to input directory containing haar cascades")
args = vars(ap.parse_args())




# initialize a dictionary to store our haar cascade detectors
print("[INFO] loading haar cascades...")


detector = cv2.CascadeClassifier(args["cascade"])




# # initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
# loop over the frames from the video stream






while True:
	# grab the frame from the video stream, resize it, and convert it
	# to grayscale
	frame = vs.read()
	frame = cv2.resize(frame, (512, 384))
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# perform face detection using the appropriate haar cascade


	rect = detector.detectMultiScale(
		gray, scaleFactor=1.25, minNeighbors=5, minSize=(15, 15),
		flags=cv2.CASCADE_SCALE_IMAGE)






        	# loop over the face bounding boxes
	for (fX, fY, fW, fH) in rect:
		# extract the face ROI

		faceROI = gray[fY:fY+ fH, fX:fX + fW]
		# apply eyes detection to the face ROI


		# draw the face bounding box on the frame
		cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)


    # show the output frame
	cv2.imshow("Frame", frame)


	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()