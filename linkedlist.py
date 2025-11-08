class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        return self.head==None
    
    def insert_at_start(self,item):
        first_node = Node(item,self.head)      #starting ma insert etle linked list pachi tarat etle pehla node create karyo ema item and node na next ma ema head etle je pehla node hato enu reference aijase nava node na next ma and pachi apde linked list ma etle ke head ma apde nava node nu reference nakhi daisu. 
        # first_node.next=self.head
        self.head = first_node

    def insert_at_last(self,item):
        new_node = Node(item)
        if not self.is_empty():
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
        else:
            self.head=new_node
    
    def search(self, item):
        temp=self.head
        while temp is not None:
            if temp.item==item:
                return temp
            temp=temp.next
        return None

    def insert_after(self,temp,item):
        if temp is not None:
            new_node = Node(item,temp.next)
            temp.next=new_node

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    
    def delete_first(self):
        temp=self.head
        if temp is not None:
            temp=temp.next
   
    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def delete_item(self,item):
        if self.head is None:
            pass
        elif self.head.next is None and self.head.item==item:
            self.head=None
        else:
            temp=self.head
            if temp.item==item:
                self.head=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==item:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedListIterator:
    def __init__(self, head):
        self.current=head

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

s1=LinkedList()
s1.insert_at_start(12)
# print(s1.head.item)
# print(s1.head.next)
s1.insert_at_start(11)
s1.insert_at_last(13)
s1.insert_after(s1.search(12),14)
s1.print_list()
s1.delete_item(13)
print()
s1.print_list()
print()



for x in s1:
    print(x,end=' ')

print()