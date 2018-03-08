import numpy as np
import cv2
import PIL
from PIL import Image
import pytesseract;
import os
count=0;

f3 = open("ocr.txt","r+")

def reading(frame):
	maxWidth = 1000

	try:
		im =Image.open('test2.jpg')
		print im
		im.show()
		ratio = maxWidth/im.size[0]
		im=im.resize((maxWidth,im.size[1]*ratio),PIL.Image.BICUBIC)
		
		
	except IOError:
	    print "cannot create thumbnail for '%s'" % infile
	output_string =pytesseract.image_to_string(im)
	print output_string
	f3.write(output_string)
	f3.close()
	os.system("python reader.py")
	
def capture():
	print "here"
	cap = cv2.VideoCapture(0)
	cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,1300);
	cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,700);
	ret, frame = cap.read()
	frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	cap.release()
	cv2.imwrite('novel/page%d.jpg' %count,frame)
	reading(frame)
	

capture()

		
	
