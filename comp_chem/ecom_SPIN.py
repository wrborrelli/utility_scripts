import numpy as np
import linecache
import sys

cube_file = sys.argv[1]
time_step = sys.argv[2]

bl = 15.66

bohr_to_ang = 0.529177
zcount = 0
ycount = 0
xcount = 0

temp_line = linecache.getline(cube_file, 3).split()
atom_num = int(temp_line[0])
start = float(temp_line[1]) * bohr_to_ang
temp_line = linecache.getline(cube_file, 4).split()
axis = float(temp_line[1]) * bohr_to_ang
grid_num = float(temp_line[0])
#print('atom_num:', atom_num, 'start:', start, 'axis:', axis, 'grid_num:', grid_num)

zcom_tot = 0
ycom_tot = 0
xcom_tot = 0
total = 0

z_num = int(grid_num//6)
remainder = int(grid_num%6)
if remainder != 0:
    z_num +=1
tot_line = int(grid_num*grid_num*z_num)
#print('remainder', remainder, 'z_num', z_num, 'tot_line', tot_line)

max_num = 0
max_line = 0
max_loc = 0
for x in range(0, tot_line):
    temp_data = linecache.getline(cube_file, x+atom_num+7).split()
    temp_data = [float(i) for i in temp_data]
    if max(temp_data) > max_num:
        max_num = max(temp_data)
        max_loc = np.argmax(temp_data)
        max_line = x

#print(max_num, max_loc, max_line)

cx = (max_line-1) // (grid_num*z_num)
cy = ((max_line-1) % (grid_num*z_num)) // z_num
cz = (((max_line-1) % (grid_num*z_num)) % z_num ) * 6 + max_loc

#print(cx, cy, cz)

max_x = start + cx * axis
max_y = start + cy * axis
max_z = start + cz * axis

#print(max_x, max_y, max_z)

for x in range(0, tot_line):
    temp_data = linecache.getline(cube_file, x+atom_num+7).split()
    temp_data = [float(i) for i in temp_data]
    temp_data = [abs(i) for i in temp_data]
    if len(temp_data) == 6:
        for y in range(0, 6):	
            xcom = start + xcount * axis
            x_diff = xcom - max_x
            if x_diff > bl/2: xcom -= bl
            if x_diff < -bl/2: xcom += bl
            xcom_tot = xcom_tot + temp_data[y] * (xcom)

            ycom = start + ycount * axis
            y_diff = ycom - max_y
            if y_diff > bl/2: ycom -= bl
            if y_diff < -bl/2: ycom += bl
            ycom_tot = ycom_tot + temp_data[y] * (ycom)

            zcom = start + (zcount + y) * axis
            z_diff = zcom - max_z
            if z_diff > bl/2: zcom -= bl
            if z_diff < -bl/2: zcom += bl
            zcom_tot = zcom_tot + temp_data[y] * (zcom)
            total = total + temp_data[y]
        zcount = zcount + 6

    elif len(temp_data) == (remainder):
        for y in range(0, remainder):
            xcom = start + xcount * axis
            x_diff = xcom - max_x
            if x_diff > bl/2: xcom -= bl
            if x_diff < -bl/2: xcom += bl
            xcom_tot = xcom_tot + temp_data[y] * (xcom)

            ycom = start + ycount * axis
            y_diff = ycom - max_y
            if y_diff > bl/2: ycom -= bl
            if y_diff < -bl/2: ycom += bl
            ycom_tot = ycom_tot + temp_data[y] * (ycom)

            zcom = start + (zcount + y) * axis
            z_diff = zcom - max_z
            if z_diff > bl/2: zcom -= bl
            if z_diff < -bl/2: zcom += bl
            zcom_tot = zcom_tot + temp_data[y] * (zcom)
            total = total + temp_data[y]
        zcount = zcount + remainder
        #print(zcount)
    if zcount == grid_num:
        zcount = 0
        ycount = ycount + 1
    if ycount == grid_num:
        xcount = xcount + 1
        ycount = 0
#print total, xcom_tot

xcom_tot = xcom_tot / total
ycom_tot = ycom_tot / total
zcom_tot = zcom_tot / total

print(time_step, xcom_tot, ycom_tot, zcom_tot)
