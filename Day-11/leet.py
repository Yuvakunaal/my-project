# https://leetcode.com/problems/linked-list-cycle/description/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        a = head
        b = head
        while a and a.next:
            a = a.next.next
            b = b.next
            if a == b:
                return True
        return False