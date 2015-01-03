"""
	Author : Diljit Ramachandran <diljitpr@gmail.com>
	Date   : 3rd January,2014
	Last Modified : 3rd January,2014
	
"""
def swap(string,index1,index2):
	""""""
	temp = string[index1]
	string[index1] = string[index2]
	string[index2] = temp

def permute(string,start,end):
	""""""
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

