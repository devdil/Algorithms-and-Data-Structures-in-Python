def insertionSort(items):
    for i in xrange(len(items)):
        for j in xrange(i,0,-1):
            if compare(items[j],items[j-1]):
                exchange(items,j,j-1)
            else:
                break
    return items

def compare(item1,item2):
    if item1 < item2:
        return True
    else:
        return False
    
def exchange(items,index1,index2):
    temp = items[index1]
    items[index1] = items[index2]
    items[index2] = temp

if __name__ == "__main__":
    items = [8,3,5,1,5,2,40,8]
    print insertionSort(items)
    
