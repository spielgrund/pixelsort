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
liste_half = []
Maske = []
width, height = img.size
y_steps = 50
mult = 1
threshold_low = 180
threshold_high = 200
countdown = 0
zufall = 50
thubnail_size = int(width/2),int(height/2)
img_s = img.copy()
img_s.thumbnail(thubnail_size)
#img.show()
#print(img.size)
data = np.asarray(img, dtype="int32")
data_half = np.asarray(img_s, dtype="int32")

start_time1 = time.time()

# Get Pixels and store their xy and rgb in Liste
# for xy in np.ndindex(data.shape[:2]):           
#     if (threshold_low <(data[xy][0]+data[xy][1]+data[xy][2])/3 < threshold_high):
        
#         Liste.append([xy[0],xy[1],(data[xy][0],data[xy][1],data[xy][2]),0])

for xy in np.ndindex(data_half.shape[:2]):           
    if (threshold_low <(data_half[xy][0]+data_half[xy][1]+data_half[xy][2])/3 < threshold_high):
        
        liste_half.append([xy[0],xy[1],(data_half[xy][0],data_half[xy][1],data_half[xy][2]),0])
    

end_time1 = time.time()
print(end_time1-start_time1)

start_time2 = time.time()
# Iterate through Liste. Every Pixel in threshold(Liste) gets repeated over rand y and brightened by y*mult
for e in liste_half:
    y = 0
    rnd = random.randint(0,zufall)
    # for _ in range (y_steps+rnd):
    #     if e[0] + _ < height:       #hier muss der y check mit rein
    #         data[e[0]+_,e[1]] =  tuple(np.add(e[2], (_*mult,_*mult,_*mult))) 
            
    #     else:
    #         break
    while y < y_steps + rnd:
        if e[0]*2 + y +1 < height and e[1]*2+1 < width:
                   
            data[e[0]*2+y,e[1]*2] =  tuple(np.add(e[2], (y*mult,y*mult,y*mult)))
            data[e[0]*2+y,e[1]*2+1] =  tuple(np.add(e[2], (y*mult,y*mult,y*mult)))
            data[e[0]*2+y+1,e[1]*2] =  tuple(np.add(e[2], (y*mult,y*mult,y*mult)))
            data[e[0]*2+y+1,e[1]*2+1] =  tuple(np.add(e[2], (y*mult,y*mult,y*mult))) 
            
            y += 2
        
        else:
            break
    #countdown += 1
    #print(len(liste_half)-countdown)

end_time2 = time.time()

img = Image.fromarray(np.asarray(np.clip(data,0,255), dtype="uint8"))
img.show()
print(end_time1-start_time1)
print(end_time2-start_time2)
#img.save( outfilename )

#for loop thresh 180/200 20.6 mit countdown
#while loop


