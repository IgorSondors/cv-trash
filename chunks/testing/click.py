# import the necessary packages
import argparse
import cv2
import os
 
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
 
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
 
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow(path, image)

# construct the argument parser and parse the arguments
dir = r'C:/Users/sondors/Desktop/not_prepared'

for i in os.listdir(dir):
	path = os.path.join(dir,i)
	image = cv2.imread(path)
	clone = image.copy()
	cv2.namedWindow(path, cv2.WINDOW_NORMAL)
	cv2.setMouseCallback(path, click_and_crop)

	# keep looping until the 'q' key is pressed
	while True:
		# display the image and wait for a keypress
		cv2.imshow(path, image)
		key = cv2.waitKey(1) & 0xFF

		# if the 'r' key is pressed, reset the cropping region
		if key == ord("r"):
			image = clone.copy()

		# if the 'c' key is pressed, break from the loop
		elif key == ord("c"):
			break

	# if there are two reference points, then crop the region of interest
	# from teh image and display it
	if len(refPt) == 2:
		roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
		cv2.imshow("ROI", roi)
		#cv2.imwrite(i, roi)
		cv2.waitKey(0)

	'''	# Поиск длины и ширины варпа
    x = [refPt[i][0] for i in range(4)]
    x_max = max(x) - min(x)
    y = [refPt[i][1] for i in range(4)]
    y_max = max(y) - min(y)

    # Делаем варп преобразование исходного изображения
    pts1 = np.float32(refPt)
    pts2 = np.float32([[0,0],[x_max,0],[x_max,y_max],[0,y_max]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    img = cv2.imread(path,3) 
    dst = cv2.warpPerspective(img,M,(x_max,y_max))
    #print('dst is:', dst)
    cv2.imshow('warp', dst)'''


	# close all open windows
cv2.destroyAllWindows()