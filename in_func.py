# FUNCTION results_to_array converting data from headered file into an 

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
            Z.append(Data[0])
            X.append(Data[1])
            Y.append(Data[2])
    print Z[0:4]
    print X[0:4]
    print Y[0:4]

    ## Create an Array combing Phase, x-, y-coords
    ARRAY=np.column_stack((Z, X, Y))
    print len(ARRAY)
    return ARRAY

