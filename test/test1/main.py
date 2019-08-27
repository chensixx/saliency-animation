# include <opencv2/imgcodecs.hpp>
import cv2 as cv
import os
import array as arr
import numpy as np
from matplotlib import pyplot as plt



a = arr.array('i', [])
imgs_train_path = "predictions/"
images = [imgs_train_path + f for f in os.listdir(imgs_train_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
images.sort()
size = len(images) - 1
img = cv.imread(images[0])
height, width = img.shape[:2]
total = height*width

for x in range(size):
   src1 = cv.imread(images[x],0   )
   src2 = cv.imread(images[x+1],0  )
   
   res = cv.subtract(src2, src1);
   #res = np.abs(src2 - src1)

   ##inverting image
   diff = ~src1
   diff=diff - src1
   #cv.imwrite("diff.png",diff)
   diff = ~diff  
   maxc=cv.countNonZero(diff)
   #print(maxc)

   # plt.hist(res.ravel(),256,[0,100])
   # plt.show()
   #print(x)

   #res = cv.inRange(res,7,10)
   white = cv.countNonZero(res)
   #print(white)
   #a.append(white*100/maxc)
   a.append(white*100/total)
   name = "new"+'%s' % x+".png"
   cv.imwrite("diff/"+ name, res)

#print(len(a))
# max_ = 0
# for x in range((len(a))):
#    if a[x] > max_ :
#       max_ = a[x]

# print(max_)
# for x in range((len(a))):
#    a[x] = (a[x]*100/max_)

print(a)





