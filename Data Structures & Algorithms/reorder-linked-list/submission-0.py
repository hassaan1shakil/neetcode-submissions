# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # naive approach using stack
        stack = []
        dummy = head
        count = 0

        while dummy:
            stack.append(dummy)
            dummy = dummy.next
            count += 1

        i = 1
        mid = count // 2
        while i <= mid:
            temp = head.next

            head.next = stack.pop()
            head = head.next

            head.next = temp
            head = head.next
            
            i += 1

        head.next = None
