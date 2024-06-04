import numpy as np
import random
import numpy as np
import os
from PIL import Image
import time

file_path = os.path.dirname(os.path.realpath(__file__))
img = Image.open(file_path + "\\spheres_v3_small.jpg")
img.load()
data = np.asarray(img, dtype="int16")

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
          #random length
        liste_half.append([xy[0],xy[1],(data_half[xy][0],data_half[xy][1],data_half[xy][2])])
    

end_time1 = time.time()
print(end_time1-start_time1)

start_time2 = time.time()

# Iterate through Liste. Every Pixel in threshold(Liste) gets repeated over rand y and brightened by y*mult
for e in liste_half:
    #y = 0
    tup1 = (0,0,0)
    rnd = random.randint(0,zufall)+y_steps
    for y in range (rnd):
        if e[0]*2 + y +1 < height and e[1]*2+1 < width:

            if (tup1[0]+tup1[1]+tup1[2] <= 760): 
                tup1 =  np.add(e[2], (y*mult,y*mult,y*mult)) # Zeitfresser
            
            xx = e[0]*2+y
            yy =  e[1]*2   
            data[xx,yy] =  tup1
            data[xx,yy+1] =  tup1
            data[xx+1,yy] =  tup1
            data[xx+1,yy+1] =  tup1
            
        else:
            break

    #tup1 = (0,0,0)
    # while y < e[3]:
    #     if e[0]*2 + y +1 < height and e[1]*2+1 < width:

    #         if (tup1[0]+tup1[1]+tup1[2] <= 760): 
    #             tup1 =  np.add(e[2], (y*mult,y*mult,y*mult)) # Zeitfresser
            
    #         xx = e[0]*2+y
    #         yy =  e[1]*2   
    #         data[xx,yy] =  tup1
    #         data[xx,yy+1] =  tup1
    #         data[xx+1,yy] =  tup1
    #         data[xx+1,yy+1] =  tup1
            
    #         y += 2
        
    #     else:
    #         break
    #countdown += 1
    #print(len(liste_half)-countdown)

end_time2 = time.time()
print(end_time1-start_time1)
print(end_time2-start_time2)

img = Image.fromarray(np.asarray(np.clip(data,0,255), dtype="uint8"))
img.show()

#img.save( outfilename )

#for loop thresh 180/200 20.6 mit countdown
#while loop


