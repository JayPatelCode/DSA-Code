class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None


    def insert_at_head(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
            return
        
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

    def append(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp



    def insert_at_between(self,val,pos):
        new_node=Node(val)
        if pos == 0:
            self.insert_at_between(val)

        temp=self.head
        count=0
        while temp.next and count<pos-1:
            count+=1
            temp=temp.next
        
        if temp is None:
            print("Position out of bounds")
            return
        
        new_node.next=temp.next
        new_node.prev=temp
        if temp.next:
            temp.next.prev=new_node
        temp.next=new_node

    def traverse_forward(self):
        temp=self.head
        while temp:
            print(temp.val, end=" ")
            temp=temp.next
        print()

    def traverse_backward(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.val, end=" ")
            temp=temp.prev
        print()

    def delete_head(self):
        if self.head is None:
           
            return None
        if self.head.next is None:
            self.head=None
            return 
        self.head=self.head.next
        self.head.prev=None
        
    def delete_last_node(self):
        if self.head is None:
            self.head=None
            return
        if self.head.next is None:
            self.head = None
            return None
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    
    def delete_in_between(self,pos):
        if self.head is None:
            print("List is empty")
            return
        if pos==0:
            self.delete_head()
            return
        temp=self.head
        count=0
        while temp and count<pos:
            count+=1
            temp=temp.next
        if temp is None:
            print("Position out of bounds")
            return

        if temp.next is None:
            self.delete_last_node()
            return
        
        temp.prev.next=temp.next
        temp.next.prev=temp.prev

n1=Node(20)
n2=Node(15)
n3=Node(40)
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2

s1=DoublyLinkedList()
s1.append(10)
s1.append(20)
s1.append(30)
# s1.traverse_forward()

# s1.insert_at_head(5)
# s1.traverse_forward()

# s1.insert_at_between(25,3)
# s1.traverse_forward()

# s1.delete_head()
# s1.traverse_forward()

s1.traverse_forward()
s1.delete_last_node()
s1.traverse_forward()