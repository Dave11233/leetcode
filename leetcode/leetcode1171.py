class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head) -> ListNode:
        if not head:
            return None
        arr = [i for i in head if i != 0]
        # while head:
        #     if head.val != 0:
        #         arr.append(head.val)
        #     head = head.next
        while True:
            cumsum = [0] * len(arr)
            cumsum[0] = arr[0]
            for i in range(1, len(arr)):
                cumsum[i] = cumsum[i - 1] + arr[i]
            if 0 in cumsum:
                index = cumsum.index(0)
                arr = arr[index + 1:]
            else:
                flag = False
                for i in range(len(arr) - 1):
                    if flag:
                        break
                    for j in range(i + 1, len(arr)):
                        if cumsum[j] - cumsum[i] + arr[i] == 0:
                            arr = arr[:i] + arr[j+1:]
                            flag = True
                            break
                if not flag:
                    # head_list = ListNode(0)
                    # p = head_list
                    # for val in arr:
                    #     q = ListNode(val)
                    #     p.next = q
                    #     p = q
                    return arr


if __name__ == '__main__':
    print(Solution().removeZeroSumSublists([1, 2, 3, -3, 4]))
