def bubbleSort(items):
	for i in range(len(items)):
		for j in range(len(items)-i-1):
			if items[j] > items[j+1]:
				items[j],items[j+1] = items[j+1],items[j]
	return items

if __name__ == "__main__":
	items = [8,3,7,2,4,10,1,6,5,9]
	print bubbleSort(items)
