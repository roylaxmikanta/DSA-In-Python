from collections import deque

list=deque([])

list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.appendleft(50)
list.appendleft(60)
print(list)
list.popleft()  
print(list)
(list.reverse())
print(list)