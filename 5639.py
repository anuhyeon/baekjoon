from __future__ import annotations
from typing import Any,Type
import sys
sys.setrecursionlimit(10**4)
class Node:
#이진 검색 트리의 노드
    def __init__(self,key:Any,value:Any,left:Node=None,right:Node=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def search(self,key:Any) -> Any:
        # 키가 key인 노드를 검색 같은 키 중복 안됨 키는 고유 번호라고 생각하면도;ㅁ
        p = self.root #루트에 주목
        
        while True:
            if p is None:
                return None
            
            if p.key == key:
                return p.value
            elif p.key < key:
                p = p.right
            elif p.key > key:
                p = p.left
        
    def add(self,key:Any,value:Any) -> bool:
        #키가 key이고 값이 value인 노드를 삽입
        def _add(node,key,value):
            # node를 루트로 하는 서브트리에 key,value 삽입
            if node.key == key:
                return False
            
            elif node.key > key:
                if node.left is None:
                    node.left = Node(key,value,None,None)
                else:
                    _add(node.left,key,value)
            elif node.key < key:
                if node.right is None:
                    node.right = Node(key,value,None,None)
                else:
                    _add(node.right,key,value)
                    
            return True
        
        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else:
            return _add(self.root,key,value)
               
    def postorder(self): # 왼 -> 오 -> 가운데
        
        def _postorder(node):
            if node.left is not None:
                _postorder(node.left)
            if node.right is not None:
                _postorder(node.right)
            print(node.key)
        
        # if self.root == None:
        #     return False
        
        _postorder(self.root)
        
    def dump(self):
        #모든 키를 오름차순으로 출력
        def print_subtree(node):
            if node is not None:
                print_subtree(node.left)
                print(node.key,":",node.value)
                print_subtree(node.right)
        
        print_subtree(self.root)
        

if __name__ == "__main__":
    arr = []
    value = 0
    BT = BinarySearchTree()
    
    while True:
        try:
            arr.append(int(sys.stdin.readline().rstrip()))
        except:
            break
    
    for key in arr:

        BT.add(key,value)
    
    #BT.dump()
    BT.postorder()
    #print(BT.root.key)

        