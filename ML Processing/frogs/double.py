import os
import cv2

max = 0
for file in os.listdir('ML Processing/frogs/frogs_processed'):
    f = int(file.replace('.jpg',''))
    if f>max: max = f
print(max)

for i in range(max):
    if i<10:
        img = cv2.imread('ML Processing/frogs/frogs_processed/{}.jpg'.format('000'+str(i)))
    elif i<100:
        img = cv2.imread('ML Processing/frogs/frogs_processed/{}.jpg'.format('00'+str(i)))
    else:
        img = cv2.imread('ML Processing/frogs/frogs_processed/{}.jpg'.format('0'+str(i)))
    img_flipped = cv2.flip(img,1)
    cv2.imwrite('ML Processing/frogs/frogs_queue/thing{}.jpg'.format(str(i)), img_flipped)