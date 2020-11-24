# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, p: ListNode, q: ListNode) -> ListNode:
        ans = ListNode(None)
        ptr = ans
        carry = sum = 0

        while(p!=None or q!=None):
            sum = carry
            if p != None:
                sum += p
                p = p.next
            if q != None:
                sum += q
                q = q.next
            carry = sum//10
            ptr.next = sum%10
            ptr = ptr.next

        if carry == 1:
            ptr.next = ListNode(carry)

        return ans.next
        



            
        