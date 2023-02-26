# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:

# Input: head = [1,2,2,1]
# Output: true

# Example 2:

# Input: head = [1,2]
# Output: false

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

# Solution video: https://www.youtube.com/watch?v=yOzXms1J6Nk

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append[head.val]
            head = head.next
        l, r = 0, len(nums) -1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True

# Follow up: Could you do it in O(n) time and O(1) space?
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Find middle (slow)
        while fast and fast.next:
            fast = head.next.next
            slow = head.next
        
        # Reverse second half
        prev = None
        while slow:
            tmp = snow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True