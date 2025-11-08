class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class StackUsingSinglyLinkedlist:
    def __init__(self):
        self.head=None

    def push(self,val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        
    def pop(self):
        if self.head==None:
            print("stack is already empty")
            return 
        ele=self.head.val
        self.head=self.head.next
        return ele

    def peek(self):
        if self.head==None:
            print("stack is already empty")
            return 
        ele=self.head.val
        return ele

    def is_empty(self):
        return (self.head==None)

    def display(self):
        if self.head==None:
            print("stack is already empty")
            return 
        temp=self.head
        data=[]

        while temp:
            data.append(temp.val)
            temp=temp.next
        return data
    
st=StackUsingSinglyLinkedlist()
print(st.pop())


st.push(13)
st.push(14)
st.push(15)
print(st.display())
print(st.pop())
print(st.peek())
print(st.display())
# print(st.)





















# Before:
# head → ┌────┬────┐
#        │ 10 │ ●──┼──→ NULL
#        └────┴────┘

# Step 1: Create new node
# ┌────┬────┐
# │ 20 │ ?  │
# └────┴────┘

# Step 2: Point new node to current head
# ┌────┬────┐    ┌────┬────┐
# │ 20 │ ●──┼──→ │ 10 │ ●──┼──→ NULL
# └────┴────┘    └────┴────┘

# Step 3: Update head to new node
#        ┌────┬────┐    ┌────┬────┐
# head → │ 20 │ ●──┼──→ │ 10 │ ●──┼──→ NULL
#        └────┴────┘    └────┴────┘
#        (TOP)          (BOTTOM)