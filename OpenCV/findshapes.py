import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser();
ap.add_argument("-i", "--image", help="path to image file")
#ap.add_argument("-c", "--color", help="color to find")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#color = (args["color"])

#print color

#cv2.imshow("Image", image)
###Count Green Squares
lower = np.array([0,255,0])
upper = np.array([0,255,0])
shapeMask = cv2.inRange(image, lower, upper)
(cnts, _) = cv2.findContours(shapeMask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print ("I found %d Green Bullish Boxes") % (len(cnts))

###Count Red Squares

lower = np.array([0,0,255])
upper = np.array([0,0,255])
shapeMask = cv2.inRange(image, lower, upper)
(cnts, _) = cv2.findContours(shapeMask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print ("I found %d Red Bearish Boxes") % (len(cnts))

###Count Blue Squares

lower = np.array([255,0,0])
upper = np.array([255,0,0])
shapeMask = cv2.inRange(image, lower, upper)
(cnts, _) = cv2.findContours(shapeMask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print ("I found %d Blue Undecided Boxes") % (len(cnts))


#cv2.imshow("Mask", shapeMask)

#input("Press a key")

#for c in cnts:
#	cv2.drawContours(image,[c], -1, (0,255,0),2)
#	cv2.imshow("Image",image)
#	cv2.waitKey(0)