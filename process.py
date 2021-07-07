import os 
import cv2

print("\n\nWhich class do you want to process?\n\nOptions: ")
[print(file) for file in os.listdir('ML Processing')if file!='.vscode']
fileset = input('\n')
print(fileset)

# Rename
def rename(fileset):
    max = 0
    loc = 'ML Processing/{set_}/{set_}_sorted'.format(set_ = fileset)
    print(loc)
    for file in os.listdir(loc):
        f = int(file.replace('.jpg',''))
        if f>max: max = f
        print(file)
    print(max)

    for i, name_i in enumerate(os.listdir('ML Processing/{set_}/{set_}_queue'.format(set_ = fileset))):
        name_f = '0'*(3-len(str(i+max)))+str(i+max)+'.jpg'
        src = 'ML Processing/{set_}/{set_}_queue/'.format(set_ = fileset) + name_i
        name_f = 'ML Processing/{set_}/{set_}_sorted/'.format(set_ = fileset) + name_f
        os.rename(src,name_f)

# crop
def crop(fileset):
    # determine dimensions
    for file in os.listdir('ML Processing/{set_}/{set_}_sorted'.format(set_ = fileset)):
        img = cv2.imread('ML Processing/{set_}/{set_}_sorted/%s'.format(set_ = fileset) %file)
        height,width,_ = img.shape
        dim = min(width,height)
        center = [height/2,width/2]
        x = center[1] - dim/2
        y = center[0] - dim/2
        crop_img = img[int(y):int(y+dim), int(x):int(x+dim)]

    #resize
    for file in os.listdir('ML Processing/{set_}/{set_}_sorted'.format(set_= fileset)):
        img = cv2.imread('ML Processing/{set_}/{set_}_sorted/%s'.format(set_ = fileset) %file)
        height,width,_ = img.shape
        if height==width:
            resize_img = cv2.resize(img,(255,255),interpolation=cv2.INTER_AREA)
            cv2.imwrite('ML Processing/{set_}/{set_}_processed/%s'.format(set_ = fileset)%file,resize_img)

    #check
    for file in os.listdir('ML Processing/{set_}/{set_}_processed'.format(set_ = fileset)):
        img = cv2.imread('ML Processing/{set_}/{set_}_processed/%s'.format(set_ = fileset)%file)
        print(img.shape)

rename(fileset)
crop(fileset)