import sys
import cv2
import numpy

output = sys.argv

"""
    Show help error with -h or empty execution
"""
if len(sys.argv) == 1 or sys.argv[0] == '-h':
    fp = open('data/help/help.txt', 'r')
    try:
        output = fp.read(-1)
    finally:
        fp.close()
else:
    # load intput data
    img = cv2.imread('data/LPlates/040603/P6040007.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 70, 150, cv2.THRESH_BINARY)

    cv2.imshow('img', thresh)
    cv2.imshow('img_original', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # load training data

    # preprocess training inputs

    # create our model and train it

    # extract information from test image and evaluate model

    pass


print(output)

