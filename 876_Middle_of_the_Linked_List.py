class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=ListNode(head.val,head.next)
        slow=ListNode(head.val,head.next)
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
        return slow
            
