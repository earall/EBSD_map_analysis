import in_func
import ph_key_func

def rapid_func(filename):
    
### Calling functions
    print 'running phase key...'
    key=ph_key_func.phase_key(filename)
    print '*******************'
    print 'running results...'
    data=in_func.results_to_array(filename)
    return data, key
