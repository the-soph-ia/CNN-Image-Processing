# rename photo files in sequential order
import os

max = 0
for file in os.listdir('ML Processing/tortoises/tortoises_sorted'):
    f = int(file.replace('.jpg',''))
    if f>max: max = f
print(max)

for i, name_i in enumerate(os.listdir('ML Processing/tortoises/tortoises_queue')):
    name_f = '0'*(3-len(str(i+max)))+str(i+max)+'.jpg'
    src = 'ML Processing/tortoises/tortoises_queue/' + name_i
    name_f = 'ML Processing/tortoises/tortoises_sorted/' + name_f
    os.rename(src,name_f)