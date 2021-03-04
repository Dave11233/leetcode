from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:

        if not root:
            return []
        p = root
        length = 0
        while p:
            length += 1
            p = p.next
        final_length, mod = divmod(length, k)
        result = []
        p = root
        for i in range(k):
            temp_length = final_length
            temp_p = p
            while temp_length > 0 and p:
                p = p.next
                temp_length -= 1
            if mod:
                p = p.next
                mod -= 1
            q = p.next
            p = p.next
            q.next = None
            result.append(temp_p)
        return result if len(result) == k else result + [None]*(k - len(result))



