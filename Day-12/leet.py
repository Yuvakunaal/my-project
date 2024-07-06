# https://leetcode.com/problems/palindrome-linked-list/description/ 
class Solution:
   def isPalindrome(self, head: Optional[ListNode]) -> bool:
       a = []
       cur = head
       while cur:
           a.append(cur.val)
           cur = cur.next
       return a==a[::-1]

# https://leetcode.com/problems/remove-linked-list-elements/description/ 
class Solution:
   def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       if not head:
           return head
       a = []
       cur = head
       while cur:
           a.append(cur.val)
           cur = cur.next
       b = [i for i in a if i!=val]
       return self.arr_to_listnode(b)
  
   def arr_to_listnode(self,arr):
       if not arr:
           return None
       head = ListNode(arr[0])
       cur = head
       for i in range(1,len(arr)):
           cur.next = ListNode(arr[i])
           cur = cur.next
       return head

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/ 
class Solution:
   def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       if not head:
           return head
       a = []
       cur = head
       while cur:
           a.append(cur.val)
           cur = cur.next
       a.pop(-n)
       return self.arr_to_listnode(a)
   def arr_to_listnode(self,arr):
       if not arr:
           return None
       head = ListNode(arr[0])
       cur = head
       for i in range(1,len(arr)):
           cur.next = ListNode(arr[i])
           cur = cur.next
       return head

# https://leetcode.com/problems/odd-even-linked-list/description/ 
class Solution:
   def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head:
           return head
       a = []
       cur = head
       while cur:
           a.append(cur.val)
           cur = cur.next
       odd,even = [],[]
       for i in range(len(a)):
           if i%2==0:
               odd.append(a[i])
           else:
               even.append(a[i])
       return self.arr_to_listnode(odd+even)
      
   def arr_to_listnode(self,arr):
       if not arr:
           return None
       head = ListNode(arr[0])
       cur = head
       for i in range(1,len(arr)):
           cur.next = ListNode(arr[i])
           cur = cur.next
       return head

# https://leetcode.com/problems/reorder-list/description/
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, node = None, slow
        while node:
            prev, node.next, node = node, prev, node.next

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

# https://leetcode.com/problems/partition-list/description/
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
           return head
        a,b = [],[]
        cur = head
        while cur:
            if cur.val < x:
                a.append(cur.val)
            else:
                b.append(cur.val)
            cur = cur.next
        return self.arr_to_listnode(a+b)
    def arr_to_listnode(self,arr):
       if not arr:
           return None
       head = ListNode(arr[0])
       cur = head
       for i in range(1,len(arr)):
           cur.next = ListNode(arr[i])
           cur = cur.next
       return head

# https://leetcode.com/problems/swap-nodes-in-pairs/description/
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
           return head
        a = []
        cur = head
        while cur:
            a.append(cur.val)
            cur = cur.next

        for i in range(0, len(a) - 1, 2):
            a[i], a[i + 1] = a[i + 1], a[i]
        return self.arr_to_listnode(a)

    def arr_to_listnode(self,arr):
       if not arr:
           return None
       head = ListNode(arr[0])
       cur = head
       for i in range(1,len(arr)):
           cur.next = ListNode(arr[i])
           cur = cur.next
       return head
