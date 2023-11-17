import numpy as np
import random
import numpy as np
from PIL import Image


img = Image.open("spheres_v3_small.jpg")
img.load()
data = np.asarray(img, dtype="int32")

Liste = []  # [0,0,(0,0,0)]
width, height = img.size
y_steps = 50
mult = 1
threshold = 200
countdown = 0
zufall = 50

# Get Pixels and store their xyy and rgb in Liste
for xy in np.ndindex(data.shape[:2]):           
    if (data[xy][0]+data[xy][1]+data[xy][2])/3 > threshold:
        
        Liste.append([xy[0],xy[1],(data[xy][0],data[xy][1],data[xy][2])])


# Iterate through Liste. Every Pixel in threshold gets repeated over rand y and brightened by y*mult
for e in Liste:
    y = 0
    rnd = random.randint(0,zufall)
    while y < y_steps + rnd:
        if e[0] + y < height:
            data[e[0]+y,e[1]] =  tuple(np.add(e[2], (y*mult,y*mult,y*mult))) 
            
            y += 1
        else:
            break
    countdown += 1
    print(len(Liste)-countdown)


img = Image.fromarray(np.asarray(np.clip(data,0,255), dtype="uint8"))
img.show()
#img.save( outfilename )




