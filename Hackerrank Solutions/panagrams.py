""""
Author : Diljit Ramachandran
Date : 8th January,2015
Problem Link : https://www.hackerrank.com/challenges/pangrams
Solution Complexity : O(n)
"""
def isPangram(input):
    alphabet_counter = [0 for x in xrange(0,26)]
    index = 0
    for x in input:
        if x == ' ':
            continue
        pos = ord(x)-ord('a')
        alphabet_counter[pos] = alphabet_counter[pos]+1
    for x in alphabet_counter:
        if x==0:
            return False
    return True
    

if __name__ == "__main__":
    input = raw_input().lower();
    input.s
    if isPangram(input):
        print "pangram",
    else:
        print "not pangram",