def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    # For example:
    # If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
    # If aDict = {1: 1, 2: 1, 3: 1} then your function should return []
    keys = []
    for i in range(len(aDict.values())):
        count = 0
        for j in range(i+1, len(aDict.values())):
            if aDict.values()[i] == aDict.values()[j]:
                break
            else: 
                count += 1
        for k in range(i):
            if aDict.values()[i] == aDict.values()[k]:
                break
            else:
                count += 1
        if count == (len(aDict.values()) - 1):
            keys.append(aDict.keys()[i])
    return sorted(keys)
