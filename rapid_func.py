def rapid_func(filename):
    

### Calling functions
    %run in_func.py
    %run ph_key_func.py
    
    print 'running phase key...'
    key=phase_key(filename)
    print '*******************'
    print 'running results...'
    data=results_to_array(filename)
    return data, key
