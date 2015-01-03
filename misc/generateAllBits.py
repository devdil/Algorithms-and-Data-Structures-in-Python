"""
    Author : Diljit Ramachandran <diljitpr@gmail.com>
    Date:3rd January 2015, 3:43 PM
    Last Modified:3rd January 2015.


"""
def generate(items,n):
    """
            @param items : the items to be permuated
            @param n: the length of the string 
            
            @return: prints all permuations of a string
    
    """
    if n < 1:
        #print "items(%d)"%n
        print items
    else:
        #print "items[%d-1] = 0"%n
        items[n-1] = 0
        #print "generate(items,%d-1)" %n
        generate(items,n-1)
        #print "items[%d-1] = 1 "%n
        items[n-1] = 1
        # print "generate(items,%d-1)" %n
        generate(items,n-1)
    
if __name__ == "__main__":
    items = [0,0,0]
    generate(items,len(items))        

