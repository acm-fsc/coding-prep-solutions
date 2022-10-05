# Author: Kyoshi Noda
# Link: https://leetcode.com/problems/linked-list-cycle/

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(self, head: Optional[ListNode]) -> bool:
    hashSet = {} #node -> index
    current = head
    index = 0
    while current:
        if current in hashSet:
            return True
        hashSet[current] = index
        current = current.next
        index += 1
    return False