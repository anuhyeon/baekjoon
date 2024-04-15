from __future__ import annotations
from typing import Any,Type
import sys

n = int(sys.stdin.readline().rstrip())
tree = {}
for i in range(n):
    root, left, right = map(str,sys.stdin.readline().split())
    tree[root] = left, right

def postorder(value):
    if value != '.':
        postorder(tree[value][0])
        postorder(tree[value][1])
        print(value,end="")
        
def preorder(value):
    if value != '.':
        print(value,end="")
        preorder(tree[value][0])
        preorder(tree[value][1])
               
def inorder(value):
    if value != '.':
        inorder(tree[value][0])
        print(value,end="")
        inorder(tree[value][1])
         

preorder('A')
print("")
inorder('A')
print("")
postorder('A')
print("")

    
        
        
        
      
    
   
        
        
   
    
        