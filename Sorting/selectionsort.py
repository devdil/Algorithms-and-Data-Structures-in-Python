def selectionsort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1,len(array)):
            if(array[j] < array[minimum]):
                minimum = j
        exchange(array,minimum,i)
    return array

def exchange(array,j,i):
    temp = array[i]
    array[i] = array[j]
    array[j]= temp

if __name__ == "__main__" :
    array = [8,9,7,1,2,3,5,4,6]
    output = selectionsort(array)
    print output
