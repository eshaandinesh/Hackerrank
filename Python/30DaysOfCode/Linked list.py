

    def insert(self,head,data): 
    #Complete this method
        
        if head == None :
            head = Node(data)
        else :
            current = head
            while current.next:
                current = current.next
            current.next = Node(data)
        return head        

