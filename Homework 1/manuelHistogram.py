import numpy as np
import cv2 as cv

#Reading image
img = cv.imread("test1.jpg",0)

#Manual histogram equalization
def manualHistogramEqualization(image, width=None, height=None):
    #Compute the histogram
    histogram,bins = np.histogram(image.flatten(), 256, [0,256])
    
    #Normalize
    normalizedHistogram = histogram / histogram.sum()

    #Compute the cumulative distribution function
    cdf = 255 * normalizedHistogram.cumsum()  
    
    #Map
    equalizedImage = cdf[image].astype(np.uint8)
    
    return equalizedImage

output_1 = manualHistogramEqualization(img)

output_2 = cv.equalizeHist(img)

result = abs(output_1 - output_2)

cv.imshow("Result",result)
cv.waitKey()
cv.destroyAllWindows()

#Mert Can Gönen
#181101039