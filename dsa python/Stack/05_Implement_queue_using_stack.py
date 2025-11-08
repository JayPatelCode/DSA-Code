
class QueueUsingStack:
    def __init__(self):
        self.s1=[]
        self.s2=[]


    def enqueue(self,item):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if not self.s1:
            print("Stack is already empty")
            return
        return self.s1.pop()
    
    def front(self):
        if not self.s1:
            print("Stack is already empty")
            return
        return self.s1[-1]
q1=QueueUsingStack()
q1.enqueue(12)
q1.enqueue(13)
q1.enqueue(14)
print(q1.front())
print(q1.s1)


q1.dequeue()
print(q1.front())

print(q1.s1)











# push(x) 
# (Note here we will have 2 stack s1 and s2)
# step 1: move all elements from s1 to s2
# step 2: insert element in s1
# step3: move all elements from s2 to s1

# pop(x)
# remove the top most element from the stack that will be front of queue

# front(x)
# the top most element from the stack that will be front of queue





# Tc: push: O(2N)
#     pop: O(1)
#     peek: O(1)