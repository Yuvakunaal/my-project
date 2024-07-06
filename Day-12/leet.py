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
