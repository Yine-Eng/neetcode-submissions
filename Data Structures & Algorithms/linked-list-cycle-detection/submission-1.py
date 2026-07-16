# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        behind, ahead = head, head

        while ahead and ahead.next:
            behind = behind.next
            ahead = ahead.next.next

            if behind == ahead:
                return True

        return False