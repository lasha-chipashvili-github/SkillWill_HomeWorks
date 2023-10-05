def min_val_in_dict(dict):
    '''
    Parameters
    ----------
    dict : <class 'dict'>

    Returns
    -------
    min : <class 'int'> ან <class 'float'>
    '''
    min = float('inf')
    for key in dict:
        if (isinstance(dict[key], int) or isinstance(dict[key], float)) and dict[key] <= min:
            min = dict[key]
        else:
            continue
    return min



def factorial(n):
    '''
    Parameters
    ----------
    n : <class 'int'>

    Returns
    -------
    <class 'int'>
    '''
    if n == 0:
        return 1
    return n*factorial(n-1)

if __name__ == "__main__":
    dict = {'a':1, 'b':1, 'c':99.9, 'd':"d", 'e':-10, 'f':0}
    print(min_val_in_dict(dict))
    
    print(factorial(5))