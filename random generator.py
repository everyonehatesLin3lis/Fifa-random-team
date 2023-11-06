import os
from os import listdir
import sys
import cv2
import glob
import random
import numpy as np

cv_img = []
IMAGE_FOLDER = "C:\\Users\\pelec\\Desktop\\Python\\fifa\\Teams"
filename = random.choice(os.listdir(IMAGE_FOLDER))
path = '%s/%s' % (IMAGE_FOLDER , filename)

filename = random.choice(os.listdir(IMAGE_FOLDER))
path1 = '%s/%s' % (IMAGE_FOLDER , filename)

capture = cv2.imread(path)
capture1 = cv2.imread(path1)
while True:
        imS = cv2.resize(capture, (460, 460))
        imS1 = cv2.resize(capture1, (460, 460))
        vis = np.concatenate((imS, imS1), axis=1)
        #cv2.imwrite('out.png', vis)

        cv2.imshow("Player 1", vis)
        cv2.waitKey(0)
        sys.exit()
cv2.destroyAllWindows()


    
    