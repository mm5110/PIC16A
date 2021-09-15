
def power_of_k(k, power=1):
    """
    Compute an integer power of a user-specified number k. 
    """
    # initialize
    x = 1
    
    # multiply x by k power times. 
    for i in range(power):
        x *= k
    return x
