#Author : Diljit Ramachandran
#Date : 1st January,2010
#Email : diljitpr@gmail.com
#ModifiedDate:1st January,2010
#Purpose : Implementation of a binary search tree with insert,delete,search and update key operations

class BST:
    def __init__(self,data):
        self.right= None
        self.left = None
        self.data=data
    
    def insertNode(root,node):
        """Parameters: @root - The root node of the BST
                       @node - the node to be inserted
           Operation: Inserts the node into the BinarySearch Tree rooted at @root """
        if node.data > root.data:
            if root.right == None:
                root.right = node 
            else:
                insertNode(root.left,node)
        else:
            if root.left == None:
                root.left = Node
            else:
                insertNode(root.left,node)
    def search(root,key):
        """Returns True:If the key is found in the tree else False"""
        if root == None:
            return False
        if root.data = key
            return True
        elif key > root.data:
            search(root.right,key)
        elif key < root.data:
            search(root.left,key)
    def update(root,oldKey,newKey):
            
    
        