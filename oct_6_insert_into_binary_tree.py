"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3485/

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        if not root: return TreeNode(val=val) # checking empty root 

        while(curr.left != None or curr.right != None): 
            if curr.val < val:
                if curr.right: curr = curr.right
                else: break
            elif curr.val > val:
                if curr.left: curr = curr.left
                else: break
        
        if curr.val < val:
            curr.right = TreeNode(val=val)
        else:
            curr.left = TreeNode(val=val)
        
        return root