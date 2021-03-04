class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def create(self, x):
        if not x:
            return None
        else:
            list_node = ListNode()
            p = list_node
            for val in x:
                temp_list_node = ListNode(val)
                p.next = temp_list_node
                p = temp_list_node
            return list_node.next

    def merge(self, head1, head2):
        if head1 is None or head2 is None:
            if head1 is None:
                return head2
            return head1
        list_node = ListNode(0)
        p = list_node
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        if head1 is None:
            p.next = head2
        if head2 is None:
            p.next = head1
        return list_node.next

    def search_middle_node(self, head):
        if not head or head.next is None:
            return head
        slow = head
        fast = head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.search_middle_node(head)
        right_ = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(right_)
        return self.merge(left, right)

if __name__ == '__main__':
    x = [4,2,1,3]
    solution = Solution()
    head = solution.create(x)
    head = solution.sortList(head)
    print(head)