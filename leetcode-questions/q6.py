#question https://leetcode.com/problems/binary-tree-inorder-traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversalSolution(root):
            if root:
                traversalSolution(root.left)
                ans.append(root.val)
                traversalSolution(root.right)
                
        traversalSolution(root)
        return ans
      
 
#Note : I still have no clue as to what this is and how/why this works. Need to study this more.
     #  Also I reached the point where i cannot proceed without understanding 'self' in python too.
  #     probably will be reading that before the next question
