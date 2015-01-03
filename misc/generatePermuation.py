"""
	Author : Diljit Ramachandran <diljitpr@gmail.com>
	Date   : 3rd January,2014
	Last Modified : 3rd January,2014
	
"""
def swap(string,index1,index2):
	"""
	Function swap takes three parameters(string,index,index2) and swaps the item at index with index2
	
	@param string type:list the string to be swapped
	@Param index1 type:int the index to be swapped
	@param index2 type:int the index to be swapped 
	
	"""
	temp = string[index1]
	string[index1] = string[index2]
	string[index2] = temp

def permute(string,start,end):
	"""
	This generates all the permutation of a given string
	
	@param string type:string  the string to be permuted
	@param start: type:integer the initial index of the string i.e 0 in all cases
	@param end:   type:integer the length of the string
	
	
	"""
	if start == end:
		print ''.join(string)
		
	else:
		j = start
		for x in range(j,end):
			swap(string,start,x)
			permute(string,start+1,end);
			swap(string,start,x)
	

if __name__ == "__main__":
	
	string  = list("abc")
	length = len(string)
	
	print permute(string,0,len(string))

