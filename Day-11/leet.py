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

# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2 = headA,headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1