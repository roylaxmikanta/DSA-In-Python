
from collections import deque


class Solution:
    def topView(self, root):
        # code here
        queue=deque([])
        hash_map={}
        queue.append([root,0])
        while len(queue)!=0:
            e,line=queue.popleft()
            if line not in hash_map:
                hash_map[line]=e.data
            if e.left:
                queue.append([e.left,line-1])
            if e.right:
                queue.append([e.right,line+1])
        result=[]
        hash_map=dict(sorted(hash_map.items()))
        for key in hash_map:
            result.append(hash_map[key])
        return result
            