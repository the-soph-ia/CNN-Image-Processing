# rename photo files in sequential order
# JELLYFISH
import os

max = 0
for file in os.listdir('ML Processing/jellyfish/jellyfish_sorted'):
    f = int(file.replace('.jpg',''))
    if f>max: max = f
print(max)

for i, name_i in enumerate(os.listdir('ML Processing/jellyfish/jellyfish_queue')):
    name_f = '0'*(3-len(str(i+max)))+str(i+max)+'.jpg'
    src = 'ML Processing/jellyfish/jellyfish_queue/' + name_i
    name_f = 'ML Processing/jellyfish/jellyfish_sorted/' + name_f
    os.rename(src,name_f)