# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=head
        length=0
        
        while dummy:
            length+=1
            dummy=dummy.next
        nodeToRemove = length-n-1
        dummy=head
        
        while nodeToRemove>0:
            dummy=dummy.next
            nodeToRemove-=1
        if nodeToRemove == -1:
            return head.next
        
        if dummy.next:
            nextNode=dummy.next.next
            dummy.next=nextNode
        
        return head


            







        