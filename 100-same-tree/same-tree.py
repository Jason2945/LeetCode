# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check to see if any of the value is None. If one of them is None, check if the two are equal
        if q == None or p == None:
            return (p == q)
        # If there is value, check if the value is the same
        if p.val != q.val:
            return False
        # Check the left value
        checkLeft = self.isSameTree(p.left, q.left)
        # Check the right values
        checkRight = self.isSameTree(p.right, q.right)
        # Make Sure both the left and right values are the same so we know the whole binary tree is true
        EqualOrNot = checkLeft and checkRight
        return EqualOrNot
        

        