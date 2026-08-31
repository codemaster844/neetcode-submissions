# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        midPoint=slow.next
        slow.next=None
        reversedList=self.reverseList(midPoint)
        
        while reversedList!=None:
            temp1=head.next
            temp2=reversedList.next
            head.next=reversedList
            reversedList.next=temp1
            reversedList=temp2
            head=temp1
    


    def reverseList(self,head: [ListNode])-> ListNode:
        current=head
        nextNode=None
        previous=None

        while current!=None:
            nextNode=current.next
            current.next=previous
            previous=current
            current=nextNode

        return previous 