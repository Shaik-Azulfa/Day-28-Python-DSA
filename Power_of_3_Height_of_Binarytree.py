#Power of 3
class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1
#Height of BinaryTree
class Solution:
    def height(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)
