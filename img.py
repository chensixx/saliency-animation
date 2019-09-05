# include <opencv2/imgcodecs.hpp>
import cv2 as cv
import os
import array as arr
import numpy as np
import glob
from matplotlib import pyplot as plt



a = arr.array('i', [])

images = [img for img in glob.glob("predictions/*.png")]
images.sort()
size = len(images) - 1
fst = cv.imread(images[0])
height, width = fst.shape[:2]
total = height*width

for x in range(0,size,1):
   src1 = cv.imread(images[x],0   )
   src2 = cv.imread(images[x+1],0  )
   
   res = cv.subtract(src2, src1);
   #res = np.abs(src2 - src1)
   # plt.hist(res.ravel(),256,[0,100])
   # plt.show()
   #res = cv.inRange(res,7,10)
   white = cv.countNonZero(res)
   #print(white)
   #a.append(white*100/maxc)
   a.append(white*100/total)
   name = "new"+'%s' % x+".png"
   cv.imwrite("diff/"+ name, res)

print(a)


