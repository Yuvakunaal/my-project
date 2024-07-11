# https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr = []
        arr += self.inorderTraversal(root.left)
        arr.append(root.val)
        arr += self.inorderTraversal(root.right)
        return arr

# https://leetcode.com/problems/binary-tree-preorder-traversal/
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr=[root.val]
        arr += self.preorderTraversal(root.left)
        arr += self.preorderTraversal(root.right)
        return arr

# https://leetcode.com/problems/binary-tree-postorder-traversal/
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr = []
        arr += self.postorderTraversal(root.left)
        arr += self.postorderTraversal(root.right)
        arr.append(root.val)
        return arr

# https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        res = []
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_nodes)
        return res
        
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

# https://leetcode.com/problems/same-tree/
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        def preorder(root,ans):
            if root:
                ans.append(root.val)
                preorder(root.left,ans)
                preorder(root.right,ans)
            else:
                ans.append(None)
        preorder(p,ans1)
        preorder(q,ans2)
        return ans1 == ans2

# https://leetcode.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def depthfirstsearch(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return ((left.val == right.val) and depthfirstsearch(left.left,right.right) and depthfirstsearch(left.right,right.left))
        return depthfirstsearch(root.left,root.right)

# https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left,root.right = root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

#https://leetcode.com/problems/path-sum/
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def eachsum(root,summ,arr):
            if not root:
                return False
            summ+=root.val
            if  not root.left and not root.right:
                arr.append(summ)
                return
            eachsum(root.left,summ,arr)
            eachsum(root.right,summ,arr)
        arr = []
        eachsum(root,0,arr)
        return targetSum in arr

# https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None 
        if root.val == val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else: 
            return self.searchBST(root.left, val)

# https://leetcode.com/problems/insert-into-a-binary-search-tree/
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root

# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def order(root,a):
            if root is not None:
                order(root.left,a)
                a.append(root.val)
                order(root.right,a)
        a = []
        order(root,a)
        b = []
        for i in range(len(a)-1):
            b.append(abs(a[i]-a[i+1]))
        return min(b)
        
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# https://leetcode.com/problems/binary-tree-maximum-path-sum/
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def maxPathSumHelper(node):
            if not node:
                return 0
            left_max = max(0, maxPathSumHelper(node.left))
            right_max = max(0, maxPathSumHelper(node.right))
            max_path_through_node = node.val + left_max + right_max
            self.max_sum = max(self.max_sum, max_path_through_node)
            return node.val + max(left_max, right_max)
        maxPathSumHelper(root)
        return self.max_sum

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root