import numpy as np
import linecache
import math
import sys
from os.path import exists

h_mass = 1.00784
o_mass = 15.999	

bl = 15.66

bohr_to_ang = 0.529177
ecom = np.zeros(3)
start_num = 1
end_num = 99

print(start_num, "to", end_num)
count = 0

for tot in range(start_num, end_num+1):
    #get ecom of excess electron
    num = 0
    temp_line = linecache.getline('ecom_128_298K_SPIN.dat', count+1).split()
    ecom[0] = float(temp_line[1])
    ecom[1] = float(temp_line[2])
    ecom[2] = float(temp_line[3])
    num = float(temp_line[0])
    #print ecom
    
    xcount=0; ycount=0; zcount=0
    rofg = 0
    total = 0
    density_name = "../cube_128_298K/SPIN_%i.cube" % (tot)
    density_check = exists(density_name)
    if density_check == False: continue
    temp_line = linecache.getline(density_name, 3).split()
    atom_num = int(temp_line[0])
    start = float(temp_line[1]) * bohr_to_ang
    temp_line = linecache.getline(density_name, 4).split()
    axis = float(temp_line[1]) * bohr_to_ang
    
    for x in range(0, 209952):
        temp_line = linecache.getline(density_name, x+7+atom_num).split()
        temp_line = [float(i) for i in temp_line]
        temp_line = [abs(i) for i in temp_line]
        if len(temp_line) == 6:
            for y in range(0, 6):
                temp_coord = np.array([xcount*axis+start, ycount*axis+start, (zcount+y)*axis+start])

                x_diff = temp_coord[0]-ecom[0]
                if x_diff > bl/2: x_diff -= bl
                if x_diff < -bl/2: x_diff += bl
                y_diff = temp_coord[1]-ecom[1]
                if y_diff > bl/2: y_diff -= bl
                if y_diff < -bl/2: y_diff += bl
                z_diff = temp_coord[2]-ecom[2]
                if z_diff > bl/2: z_diff -= bl
                if z_diff < -bl/2: z_diff += bl

                temp_length = x_diff**2 + y_diff**2 + z_diff**2
                rofg = rofg + temp_line[y] * temp_length
                total = total + temp_line[y]
            zcount += 6
        elif len(temp_line) == 2:
            for y in range(0, 2):
                temp_coord = np.array([xcount*axis+start, ycount*axis+start, (zcount+y)*axis+start])            

                x_diff = temp_coord[0]-ecom[0]
                if x_diff > bl/2: x_diff -= bl
                if x_diff < -bl/2: x_diff += bl
                y_diff = temp_coord[1]-ecom[1]
                if y_diff > bl/2: y_diff -= bl
                if y_diff < -bl/2: y_diff += bl
                z_diff = temp_coord[2]-ecom[2]
                if z_diff > bl/2: z_diff -= bl
                if z_diff < -bl/2: z_diff += bl

                temp_length = x_diff**2 + y_diff**2 + z_diff**2
                rofg = rofg + temp_line[y] * temp_length
                total = total + temp_line[y]
            zcount += 2
        if zcount == 108:
            zcount = 0
            ycount += 1
        if ycount == 108:
            xcount += 1
            ycount = 0
        
    count+=1 

    rofg = math.sqrt(rofg / total)
    print(num, density_name, rofg)
    linecache.clearcache()



