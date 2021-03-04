class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def init(x):
        head = ListNode(x[0])
        p = head
        for i in x[1:]:
            q = ListNode(i)
            p.next = q
            p = q
        return head

    def swap(self, head: ListNode, tail: ListNode):
        x = ListNode(0)
        x.next = tail
        pre = tail
        flag = True
        while head is not None and head != tail:
            p = head.next
            head.next = x.next
            x.next = head
            if flag:
                pre = head
                flag = False
            head = p
        return x.next, pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        x = ListNode(0)
        x.next = head
        # ret_head = ListNode(0)

        pre = x
        # flag = True
        while True:
            p = pre.next
            if p is None:
                break
            index = 0
            while index < k and p is not None:
                index += 1
                p = p.next
            if p is not None:
                q = pre.next
                # temp = p.next
                p, pre_ = self.swap(head=q, tail=p)
                # if flag:
                #     ret_head = p
                #     # ret_head.next =
                #     flag = False
                pre.next = p
                pre = pre_
            else:
                if index < k:

                    break
                else:
                    q = pre.next
                    # temp = p.next
                    p, pre_ = self.swap(head=q, tail=p)
                    # if flag:
                    #     ret_head = p
                    #     # ret_head.next =
                    #     flag = False
                    pre.next = p
                    pre = pre_
                    break

        return x.next

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    head = Solution.init(x)
    solution = Solution()
    list_head = solution.reverseKGroup(head, 2)
    # print(list_head_)
    # while list_head is not None:
    #     print(list_head.val)
    #     list_head = list_head.next
