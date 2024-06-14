class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp=head
        s=""
        l=[]
        while (temp):
            s+=str(temp.val)
            temp=temp.next
        
        decimal=int(s,2)
        return decimal
