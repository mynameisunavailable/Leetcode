
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print(l1.val)
        # print(l2.val)
        res = ListNode()
        cur = res
        # carry_over = 0
        n = 0
        while l1 or l2 or (n > 0):
            if l1 != None:
                n = n + l1.val
                l1 = l1.next
            if l2 != None:
                n = n + l2.val
                l2 = l2.next
            
            # if n > 0:
            #     n = carry_over
            # else:
            #     return res.next
            
            if n <= 9:
                cur.next = ListNode(n)
            else:
                cur.next = ListNode(n % 10)
            n = n // 10
            cur = cur.next

        return res.next
