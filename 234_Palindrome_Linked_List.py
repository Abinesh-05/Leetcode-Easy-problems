class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head
        stk=[]

        while(curr):
            stk.append(curr.val)
            curr=curr.next
        
        return stk==stk[::-1]
