import numpy as np
import linecache 
import math
import sys

def linecount(target):
	count = 0
	for line in open(target).readlines(): count+=1
	return count

skip = 0
onedips = sys.argv[1]
abs_file_name = sys.argv[2]
states = 3
data_num = int(linecount(onedips)/states - skip)
times = np.zeros(data_num)
oscillator_str = np.zeros((data_num,states))
bandgap = np.zeros((data_num,states))
#print(data_num)

for x in range(0, data_num):
    tlinet = linecache.getline(onedips, states*x+1+skip*states).split()
    times[x] = float(tlinet[0])
    for y in range(0, states):
		temp_line = linecache.getline(onedips, states*x+y+1+skip*states).split()
		oscillator_str[x,y] = float(temp_line[4])
		bandgap[x,y] = float(temp_line[3])

spectrum_points = 600
spectrum_dx = 0.01
abs_spectrum = np.zeros((spectrum_points))
x_energy = np.zeros((spectrum_points))
sigma = 0.25

for x in range(0, spectrum_points):
	x_energy[x] = x*spectrum_dx + spectrum_dx/2

#count = 0
#for x in range(0, data_num, 400):
#	for y in range(0, states):
#		count += 1
#		for z in range(0, spectrum_points):
#			energy = (z-1)*spectrum_dx
#			coeff = bandgap[x,y] * oscillator_str[x,y] / math.sqrt(math.pi * sigma)
#			abs_spectrum[z] = abs_spectrum[z] + coeff * math.exp(-((x_energy[z]-bandgap[x,y])/sigma)**2)
#	print(x,'done')

for x in range(0,data_num):
    for y in range(0, states):
        for z in range(0, spectrum_points):
            energy = (z-1)*spectrum_dx
            coeff = bandgap[x,y] * oscillator_str[x,y] / math.sqrt(math.pi * sigma)
            abs_spectrum[z] = abs_spectrum[z] + coeff * math.exp(-((x_energy[z]-bandgap[x,y])/sigma)**2)
    abs_file = open(abs_file_name+'_'+str(times[x])+'.dat', 'w')
    for x in range(0, spectrum_points):
        abs_file.write('{0:.8f} {1:.8f} \n'.format(x_energy[x],abs_spectrum[x]))
    abs_file.close()

#for x in range(0, spectrum_points):
#	abs_spectrum[x] = abs_spectrum[x] / (count*3)

#print(abs_file_name)

#abs_file = open(abs_file_name, 'w')
#for x in range(0, spectrum_points):
#	abs_file.write('{0:.8f} {1:.8f} \n'.format(x_energy[x],abs_spectrum[x]))

#abs_file.close()
