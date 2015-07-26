def list_extend_many1(lists):
    result = []
    i = 0
    while i < len(lists): 
        result += lists[i]
        i += 1
    return result
 
def list_extend_many2(lists):
    result = []
    i = len(lists)
    while i >= 0:
        i -= 1
        result.extend(lists[i])
    return result
 
def list_extend_many3(lists):
    result = []
    for i in range(len(lists) - 1, -1, -1):
        result.extend(lists[i])
    return result
 
def list_extend_many4(lists):
    result = []
    i = 0
    while i < len(lists): 
        result.extend(lists[i])
        i += 1
    return result
def list_extend_many(lists):
    """Returns a list that is the concatenation of all the lists in the given list-of-lists."""
    result = []
    for l in lists:
        result.extend(l)
    return result
#print list_extend_many([[1,2], [3], [4, 5, 6], [7]])
print list_extend_many1([[1,2], [3], [4, 5, 6], [7]])
#print list_extend_many2([[1,2], [3], [4, 5, 6], [7]])
#print list_extend_many3([[1,2], [3], [4, 5, 6], [7]])
print list_extend_many4([[1,2], [3], [4, 5, 6], [7]])