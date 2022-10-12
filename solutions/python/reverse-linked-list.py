#Author: Kyoshi Noda
#Link: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    currentNode = head
    previous = None
    while currentNode:
      temp = currentNode.next
      currentNode.next = previous
      previous = currentNode
    return previous
