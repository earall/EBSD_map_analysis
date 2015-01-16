

def rapid_func(filename):
    
### Calling functions
    print 'running phase key...'
    key=phase_key(filename)
    print '*******************'
    print 'running results...'
    data=results_to_array(filename)
    return data, key
# FUNCTION results_to_array converting data from headered file into an 

import numpy as np

def results_to_array(filename):

## Read in file and find number of phases, this alters file 
    f = open (filename,'r')

    for line in f:
        if line[0:6] == 'Phases':
            R=line.split()
            print line[7]
        
    Ph_nums=float(R[1])
    Line_start=14+Ph_nums
    print Line_start

    ## NEW SEC
    f = open (filename,'r')
    X=[]
    Y=[]
    Z=[]
    for i, line in enumerate(f):
        # Read in files from line_start and beyond
        if i >= Line_start:
            Data=line.split()
            Z.append(float(Data[0]))
            X.append(float(Data[1]))
            Y.append(float(Data[2]))
    print Z[0:4]
    print X[0:4]
    print Y[0:4]

    ## Create an Array combing Phase, x-, y-coords
    ARRAY=np.column_stack((Z, X, Y))
    print len(ARRAY)
    return ARRAY

import numpy as np

def phase_key(filename):

    f = open (filename,'r')

#find number of phases
    for line in f:
        if line[0:6] == 'Phases':
            R=line.split()
        
#selecting range where phase names are
    Ph_nums=float(R[1])
    Line_a=13
    Line_b=Ph_nums+12

#create list of phases
    f = open (filename,'r')
    phase=[]
    for i, line in enumerate(f):
# Read in files from line_start and beyone
        if i >= Line_a and i <= Line_b:
            Data=line.split()
            phase.append(Data[2])
        
#create number range for phase key
    phase_num=range(1,len(phase)+1)

#combine key
    Key=np.column_stack((phase_num, phase))
    print Key
    return Key
