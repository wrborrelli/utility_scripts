import numpy as np
import sys

# $1 is onedips.out
# $2 is onedips_af.out
# $3 is new onedips_af.out filename prefix
# $4 is # of timesteps to skip for eqb

# first get rid of excess times

skip=int(sys.argv[4])

ods = np.loadtxt(sys.argv[1])
ods = ods.reshape((int(len(ods)/3),3,len(ods[0])))
rods = np.loadtxt(sys.argv[2])
rods = rods.reshape((int(len(rods)/3),3,len(rods[0])))

times,inds = np.unique(rods[:,0][:,0], return_index=True)

rods = rods[inds]

#if len(rods) != len(ods):
#    sys.exit('Total length incongruent!')
#else:
#    None

mins = np.array(list(map(np.min, rods[:,:,3])))

zero_inds = np.where(mins == 0.0)[0]

for i in zero_inds:
    told = ods[i]
    tnew = rods[i]
    if not(told[0][0] == tnew[0][0]) and not(told[1][0] == tnew[1][0]) and not(told[2][0] == tnew[2][0]):
        sys.exit('Incongruent times!')
    else:
        None
    twhere = np.where( told[:,3] == np.setdiff1d(told[:,3], tnew[:,3])[0])
    state_ind = np.where(tnew[:,3] == 0.0)[0][0]
    for j in range(3,8):
        rods[i,state_ind][j] = told[twhere][0][j]

#np.savetxt(sys.argv[3]+'.out', rods)
for i in range(3):
    np.savetxt(sys.argv[3]+'_s'+str(i+1)+'.dat', rods[skip:,i,[3,4,5,6,7]])

