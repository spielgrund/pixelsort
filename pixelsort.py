import numpy as np
import random
import numpy as np
import os
from PIL import Image
import time

file_path = os.path.dirname(os.path.realpath(__file__))
img = Image.open(file_path + "\\spheres_v3_small.jpg")
img.load()
data = np.asarray(img, dtype="int32")

Liste = []  # [0,0,(0,0,0)] x,y,rgb
width, height = img.size
y_steps = 50
mult = 1
threshold_low = 180
threshold_high = 200
countdown = 0
zufall = 50

start_time1 = time.time()

# Get Pixels and store their xy and rgb in Liste
for xy in np.ndindex(data.shape[:2]):           
    if (threshold_low <(data[xy][0]+data[xy][1]+data[xy][2])/3 < threshold_high):
        
        Liste.append([xy[0],xy[1],(data[xy][0],data[xy][1],data[xy][2])])

end_time1 = time.time()
print(end_time1-start_time1)

start_time2 = time.time()
# Iterate through Liste. Every Pixel in threshold gets repeated over rand y and brightened by y*mult
for e in Liste:
    y = 0
    rnd = random.randint(0,zufall)
    while y < y_steps + rnd:
        if e[0] + y < height:       #hier muss der y check mit rein
            data[e[0]+y,e[1]] =  tuple(np.add(e[2], (y*mult,y*mult,y*mult))) 
            
            y += 1
        else:
            break
    countdown += 1
    print(len(Liste)-countdown)

end_time2 = time.time()

img = Image.fromarray(np.asarray(np.clip(data,0,255), dtype="uint8"))
img.show()
print(end_time1-start_time1)
print(end_time2-start_time2)
#img.save( outfilename )

#first 0.06
#loop 15.3 mit print
#loop 7.765 ohne print



