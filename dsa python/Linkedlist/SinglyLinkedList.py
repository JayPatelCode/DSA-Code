class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SinglyLinkedlist:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def traverse(self):
        if self.head==None:
            print("SInglly linked list is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
            print()
    def insert_pos(self,val,index):
        new_node=Node(val)
        if index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr_node=self.head
            prev=None
            count=0
            while curr_node is not None and count<index:
                prev=curr_node
                curr_node=curr_node.next
                count+=1
            prev.next=new_node
            new_node.next=curr_node


    def delete_node(self,val):
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next

            else:
                Found=False
                prev=None
                while temp.next:
                    if temp.val==val:
                        Found=True
                        break
                prev=temp
                temp=temp.next
                if Found:
                    prev.next=temp.next
                    return
                else:
                    print("Not found")













# node1=Node(5)
# node2=Node(7)
# node3=Node(14)
# node4=Node(10)

# node1.next=node2
# node2.next=node3
# node3.next=node4
# print(node1.val)
# print(node1.next.val)
# print(node1.next.next.next.next)
# print(node4.next)
sll=SinglyLinkedlist()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(1)
sll.traverse()