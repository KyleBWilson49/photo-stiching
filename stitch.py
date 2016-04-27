# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png

# import the necessary packages
from pyimagesearch.panorama import Stitcher
import argparse
import imutils
import cv2
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('./images'):
    f.extend(filenames)
    break

imageA = "images/" + f[1]
imageB = "images/" + f[2]

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(imageA)
imageB = cv2.imread(imageB)
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
