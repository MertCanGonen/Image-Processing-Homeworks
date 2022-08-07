import cv2 as cv
import numpy as np

#Mert Can Gönen
#181101039

img = cv.imread("lena_grayscale_hq.jpg")

#QUESTION 1

def integralImage(image):
    (h,w) = image.shape[:2]
    output = np.zeros((h,w,3))
    for i in range(h):
        for j in range(w):
            tmp = 0
            pixel = [0, 0, 0]
            if (i==0 and j ==0):
                tmp = int(image[i][j][0])
            elif (i==0):
                tmp = int(output[i][j-1][0]) + int(image[i][j][0])
            elif (j==0):
                tmp = int(output[i-1][j][0]) + int(image[i][j][0])
            else:
                tmp = int(output[i][j-1][0])
                for x in range(i+1):
                    tmp = tmp + int(image[x][j][0])
            pixel = [tmp, tmp, tmp]
            output[i][j] = pixel
    output = cv.copyMakeBorder(output, 1, 0, 1, 0, cv.BORDER_CONSTANT, (0,0,0))
    return output

o1 = cv.integral(img)
o2 = integralImage(img)
result = (o1 - o2) * 100
cv.imshow("Result", result)
cv.waitKey(0)

#QUESTION 2

def boxFilter(image, kernel):
    (h,w) = image.shape[:2]
    output = np.zeros((h,w,3))
    k = int((kernel-1) / 2)
    for i in range(h):
        for j in range(w):
            tmp = 0
            ax = i+k
            ay = j+k
            bx = i+k
            by = j-(k+1)
            cx = i-(k+1)
            cy = j+k
            dx = i-(k+1)
            dy = j-(k+1)
            if (i < h-k and j < w-k): #total sum
                tmp = tmp + int(image[ax][ay][0])
            if (i >= (k+1) and j >= (k+1)): #upper left corner (we substract it twice, so we have to add)
                tmp = tmp + int(image[dx][dy][0]) 
            if (i < h-k and j >= (k+1)): #bottom left neighbour, substract it to find sum of kernel
                tmp = tmp - int(image[bx][by][0])
            if (i >= (k+1) and j < w-k): #top right neighbour, substract it to find sum of kernel
                tmp = tmp - int(image[cx][cy][0])
            if (j == w-k and i != h-1): #eger en sagdaysa nokta, total sum o kernelin o satirdaki en asagidaki elemani  
                tmp = tmp + int(image[i+k][j][0])
            if (j == w-k and i == h-1):
                tmp = tmp + int(image[i][j][0]) #eger en dipteyse, total sum elemanin kendisi
            tmp = round(tmp / kernel**2)
            print(tmp)
            tmp = int(tmp)
            pixel = [tmp, tmp, tmp]
            output[i][j] = pixel
    return output

r1 = cv.blur(o1, (3,3), cv.BORDER_CONSTANT)
r1 = r1.astype(np.uint8)
r2 = boxFilter(o1,3)


result = r1 - r2
cv.imshow("Result", result)
cv.waitKey()
cv.destroyAllWindows()
