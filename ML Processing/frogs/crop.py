# make photo 255x255
# FROGS
import os
import cv2

#crop
for file in os.listdir('ML Processing/frogs/frogs_sorted'):
    img = cv2.imread('ML Processing/frogs/frogs_sorted/%s'%file)
    height,width,_ = img.shape
    dim = min(width,height)
    center = [height/2,width/2]
    x = center[1] - dim/2
    y = center[0] - dim/2
    crop_img = img[int(y):int(y+dim), int(x):int(x+dim)]
    cv2.imwrite('ML Processing/frogs/frogs_sorted/%s'%file,crop_img)

#resize
for file in os.listdir('ML Processing/frogs/frogs_sorted'):
    img = cv2.imread('ML Processing/frogs/frogs_sorted/%s' %file)
    height,width,_ = img.shape
    if height==width:
        resize_img = cv2.resize(img,(255,255),interpolation=cv2.INTER_AREA)
        cv2.imwrite('ML Processing/frogs/frogs_processed/%s'%file,resize_img)

#check
for file in os.listdir('ML Processing/frogs/frogs_processed'):
    img = cv2.imread('ML Processing/frogs/frogs_processed/%s'%file)
    print(img.shape)
