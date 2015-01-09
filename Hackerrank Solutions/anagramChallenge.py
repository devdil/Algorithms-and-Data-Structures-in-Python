
""""
Author : Diljit Ramachandran
Date : 8th January,2015
Problem Link : https://www.hackerrank.com/challenges/pangrams
Solution Complexity : O(n)
"""
def minimumEdits(input):
    input = list(input)
    input_length = len(input)
    number_of_changes = 0
    if input_length%2 == 0:
        string1 = input[0:input_length/2]
        string2 = input[input_length/2:]
        
if __name__ == "__main__":
    test_cases = int(raw_input())
    while test_cases:
        print minimumEdits(raw_input())
        test_cases = test_cases -1

                     
