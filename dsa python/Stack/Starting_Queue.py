class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return(len(self.items)==0)
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.items==0:
            print("Queue is already empty")
            return 
        
        return self.items.pop(0)
    
    def front(self):
        if len(self.items)==0:
            print("cannot find peak, Queue is already empty")
            return 
        return self.items[0]
    
    def rear(self):
        if len(self.items)==0:
            print("cannot read, Queue is already empty")
            return 
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    

q=Queue()
q.enqueue(12)
q.enqueue(14)
print(q.front())
print(q.rear())
print(q.size())
print(q.dequeue())
print(q.front())
print(q.rear())
print(q.size())





#####dequeue takes O(N) while all other operations take O(1)