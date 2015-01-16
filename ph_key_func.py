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
    f = open ('AL001MeltsNR.ctf','r')
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
