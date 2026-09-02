

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        no = 0
        current = head

        while current is not None:
            no += 1
            current = current.next

        prv_node = dummy

        n = no // k

        for i in range(n):
            prv_node = self.reverse(prv_node, k)

        return dummy.next


    def reverse(self, first_prv_node: ListNode, k: int):

        current = first_prv_node.next
        next_node = current.next

        i = 0

        while i < k - 1:
            temp = next_node.next
            next_node.next = current
            current = next_node
            next_node = temp

            i += 1
        group_last = first_prv_node.next
        group_last.next = next_node
        first_prv_node.next = current
        return group_last