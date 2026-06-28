class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        r1 = result
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            r1.next = ListNode(total % 10)
            r1 = r1.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
           
        return result.next
