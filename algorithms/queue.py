# class Queue:
#     def __init__(self):
#         self.elements = []

#     @property
#     def is_empty(self):
#         return not len(self.elements)

#     def put(self, val):
#         self.elements.append(val)
    
#     def get(self):
#         return self.elements.pop(0)

from collections import deque
class Queue:
    def __init__(self):
        self.elements = deque()
    def empty(self):
        return not self.elements
    def put(self, data):
        self.elements.append(data)
    def get(self):
        return self.elements.popleft()

# class PriorityQueue:
#     def __init__(self):
#         # [(item, priority)]
#         self.elements = []

#     @property
#     def is_empty(self):
#         return not len(self.elements)

#     def put(self, data):
#         priority = data[0]
#         if self.is_empty:
#             self.elements.append(data)
#         else:
#             for i in range(len(self.elements)):
#                 if priority < self.elements[i][1]:
#                     self.elements.insert(i, data)
#                     break
#                 elif priority == self.elements[i][1]:
#                     self.elements.insert(i+1, data)
#                     break
#             else:
#                 self.elements.append(data)

#     def get(self):
#         if not self.is_empty:
#             return self.elements.pop(0)

import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self):
        return not self.elements
    def put(self, data): #priority, location
        heapq.heappush(self.elements, (data[0], data[1]))
    def get(self):
        return heapq.heappop(self.elements)


# myQueue = PriorityQueue()
# myQueue.put((12, 'A'))
# myQueue.put((1, "B"))
# myQueue.put((14, "C"))
# myQueue.put((1, "C"))
# myQueue.put((7, "D"))
# print(myQueue.elements)            
# while not myQueue.empty():
#     print(myQueue.get()) 