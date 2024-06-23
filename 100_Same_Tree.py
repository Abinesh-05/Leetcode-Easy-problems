class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def match(p,q):
            if not p and not q:
                return True
            
            elif not p and q or not q and p:
                return False

            elif p.val!=q.val:
                return False

            return match(p.left,q.left) and  match(p.right,q.right)
            
        return match(p,q)           
