#Mert Can Gönen
#181101039

import cv2 as cv
import numpy as np

image = cv.imread("lena_grayscale_hq.jpg")

def boxFilter(image):
    (h, w) = image.shape[:2]
    image = cv.copyMakeBorder(image, 1, 1, 1, 1, cv.BORDER_CONSTANT)
    arr = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    bline1 = np.zeros((1,w,3), dtype=np.uint8)
    check1 = False
    bline2 = np.zeros((1,w,3), dtype=np.uint8)
    check2 = False
    for i in range(1, h+1):
        for j in range(1, w+1):
            top = i - 1
            bottom = i + 1 + 1
            left = j - 1
            right = j + 1 + 1
            tmp = 0
            for x in range(top, bottom):
                for y in range(left, right):
                    tmp = tmp + (image[x][y][0] * arr[x-top][y-left])
            tmp = tmp//9
            pixel = [tmp, tmp, tmp]
            if (i % 2 == 1):
                bline1[0][j-1] = pixel
            elif (i % 2 == 0):
                bline2[0][j-1] = pixel
        if (i >= 2):
            if (i == 512):
                image[i][1:w+1] = bline2
            if (i % 2 == 0):
                if check1 is False:
                    image[i-1][1:w+1] = bline1
                    check1 = True
                    check2 = False
            else:
                if check2 is False:
                    image[i-1][1:w+1] = bline2
                    check2 = True
                    check1 = False
    image = image[1:h+1,1:w+1]
    return image

blurred = cv.boxFilter(image, -1, (3,3), borderType=cv.BORDER_CONSTANT)
x = boxFilter(image)
r = blurred - x

cv.imshow("Difference", r)
cv.waitKey(0)