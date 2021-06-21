# make photo 255x255
# ROCKS
import os
import cv2

#crop
for file in os.listdir('ML Processing/tortoises/tortoises_sorted'):
    img = cv2.imread('ML Processing/tortoises/tortoises_sorted/%s' %file)
    height,width,_ = img.shape
    dim = max(width,height)
    center = [height/2,width/2]
    x = center[1] - dim/2
    y = center[0] - dim/2
    crop_img = img[int(y):int(y+dim), int(x):int(x+dim)]
    

#resize
for file in os.listdir('ML Processing/tortoises/tortoises_sorted'):
    img = cv2.imread('ML Processing/tortoises/tortoises_sorted/%s' %file)
    height,width,_ = img.shape
    if height==width:
        resize_img = cv2.resize(img,(255,255),interpolation=cv2.INTER_AREA)
        cv2.imwrite('ML Processing/tortoises/tortoises_processed/%s'%file,resize_img)

#check
for file in os.listdir('ML Processing/tortoises/tortoises_processed'):
    img = cv2.imread('ML Processing/tortoises/tortoises_processed/%s'%file)
    print(img.shape)
