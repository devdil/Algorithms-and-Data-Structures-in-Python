def countSort(items):
	max = items[0]
	for i in range(len(items)):
		if(items[i]>max):
			max = items[i]
	index = [0]*(max+1)
	array = []
	for i in range(len(items)):
		index[items[i]]+=1
	for i in range(len(index)):
		while(index[i]):
			array.append(i)
			index[i]-=1
	return array

if __name__ == "__main__":
	items = [4,2,2,3,5,1,3,1,4,5,2,1,3,4,1,2,5,5,2]
	print countSort(items)