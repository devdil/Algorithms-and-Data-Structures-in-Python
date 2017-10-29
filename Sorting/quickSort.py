def quickSort(items):
	if not items:
		return items
	else:
		left = []
		right = []
		for i in range(1,len(items)):
			if(items[i]<items[0]):
				left.append(items[i])
			else:
				right.append(items[i])
		return quickSort(left) + [items[0]] + quickSort(right)

if __name__ == "__main__":
	items = [4,7,2,1,9,5,10,3,6,8]
	print quickSort(items)