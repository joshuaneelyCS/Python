# Given a linked list, delete duplicates

def deleteDuplicates(self, head):
        result = head

        if head == None:
            return head

        while head.next != None:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return result
