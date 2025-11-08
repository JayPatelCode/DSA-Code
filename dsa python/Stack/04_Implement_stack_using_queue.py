from collections import deque
class STQ:
    def __init__(self):
        self.items = deque()

    def push(self,item):
        self.items.append(item)
        for _ in range(len(self.items)-1):
            self.items.append(self.items.popleft())

    def pop(self):
        if len(self.items)==0:
            print("stack is already empty")
            return
        return self.items.popleft()

    def peek(self):
        if len(self.items)==0:
            print("stack is already empty")
            return
        return self.items[0]

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)


cs=STQ()
cs.push(11)
cs.push(1)
cs.push(2)
print(cs.peek()) #return 2
print(cs.pop()) # return 2
print(cs.is_empty()) # return False
print(cs.items)







# for push
# step 1 first push item in queue using append
# step 2 Rotate whole list n-1 times

# for pop
# step 1 remove oth index which we can obtain by using popleft by using O(1) time complexity







# Time and Space Complexity
# push(): O(n) – Rotating n-1 elements
# pop(): O(1)
# top(): O(1)
# empty(): O(1)
# Space: O(n) – Single queue
