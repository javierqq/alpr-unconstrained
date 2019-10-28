# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("samples/country/video/GJDB75.mp4")

try:

	# creating a folder named data
	if not os.path.exists('samples/country/video/results'):
		os.makedirs('samples/country/video/results')

# if not created then raise error
except OSError:
	print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):

	# reading from frame
    ret,frame = cam.read()
    if ret:
		# if video is still left continue creating images
        if currentframe%50 == 0:

            #clear directory to read only 1 .jpg
            os.system("rm samples/country/video/results/*")

            name = 'samples/country/video/results/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)

		    # writing the extracted images
            cv2.imwrite(name, frame)

            #run alpr
            os.system("bash run.sh -i samples/country/video/results -o /tmp/output -c /tmp/output/results_country.csv")


		# increasing counter so that it will
		# show how many frames are created
        currentframe += 1
    else:
		break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
