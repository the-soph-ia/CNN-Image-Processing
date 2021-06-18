# rename photo files in sequential order
import os

max = 0
for file in os.listdir('ML Processing/frogs/frogs_sorted/'):
    f = int(file.replace('.jpg',''))
    if f>max: max = f
print(max)

for i, name_i in enumerate(os.listdir('ML Processing/frogs/frogs_queue')):
    name_f = '0'*(4-len(str(i+max)))+str(i+max)+'.jpg'
    src = 'ML Processing/frogs/frogs_queue/' + name_i
    name_f = 'ML Processing/frogs/frogs_sorted/' + name_f
    os.rename(src,name_f)