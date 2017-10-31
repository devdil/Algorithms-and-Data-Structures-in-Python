def shellSort(items):
	n = len(items)
	x = n/2
	while x>0:
		for i in range(x,n):
			j = i
			temp = items[i]
			while j>=x and items[j-x]>temp:
				items[j] = items[j-x]
				j-=x
			items[j] = temp
		x/=2
	return items

if __name__ == "__main__":
	items = [4,7,2,1,9,5,10,3,6,8]
	print shellSort(items)