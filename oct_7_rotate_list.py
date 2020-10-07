"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3486/

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: # empty ListNode
            return head
        if head.next == None: # ListNode of length 1
            return head
        
        
        counter, curr = 1, head, 
        
        # also need to know the length of it first because want to rotate to the right
        while(curr.next != None):
            counter += 1
            curr = curr.next
        
        curr = head
        
        # cannot find out why this edge case is annoying me
        if k % counter == 0:
            return head 
        
        if k > counter:
            k = k % counter
        # going till just before the kth from the right
        for i in range(counter-k-1):
            if curr.next == None: # reached the end
                curr = head
            else:
                curr = curr.next 
        
        # adding a temp listnode to seperate at k from right
        temp = curr.next # placeholder for right section
        curr.next = None # breaking off left section from right
        
        # need to cut off second portion 
        temp2 = temp # placeholder 
        while(temp2.next != None):
            temp2 = temp2.next
        
        # merging right to left section
        temp2.next = head
        
        return temp