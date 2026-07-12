# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1) traverse to the mid of the array

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        

        # 2) reverse the later half of the list

        head2 = curr = slow.next    # head of second list (non-reversed)  
        slow.next = None            # terminate end of first list
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
            temp = temp.next if temp else None
            head2 = prev

        
        # 3) merge both lists

        while head and head2:
            temp1 = head.next
            temp2 = head2.next

            head.next = head2
            head2.next = temp1

            head = temp1
            head2 = temp2