from collections import deque

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        if root is None:
            return []
        queue=deque()
        hash_map={}
        queue.append([root,0])
        while(len(queue)!=0):
            e,line=queue.popleft()
            hash_map[line]=e.data
            if e.left:
                queue.append([e.left,line-1])
            if e.right:
                queue.append([e.right,line+1])
        hash_map=dict(sorted(hash_map.items()))
        result=[]
        for key in hash_map:
            result.append(hash_map[key])
        return result