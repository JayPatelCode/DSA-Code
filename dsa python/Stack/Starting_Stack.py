class Stack:
    def __init__(self):
        self.items=[]


    def is_empty(self):
        return len(self.items)==0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            return -1

        return self.items.pop()

    def top(self):
        if len(self.items)==0:
            return "stack is empty"
        return self.items[-1]
    def size(self):
        return len(self.items)
st=Stack()
st.push(12)
st.push(13)
st.push(15)
# st.pop()
r=st.pop()
print(r)
print(st.items)
print(st.top())



# Time and Space Complexity
# push(): O(1) per operation
# pop(): O(1) per operation
# Space: O(n) where n is the number of elements in the stack
