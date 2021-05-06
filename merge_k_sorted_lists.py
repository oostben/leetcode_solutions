# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0,None)
        temp = head
        remove = []
        for i in range(len(lists)):
            if lists[i] is None: remove.append(i)
        for index in reversed(remove):
            lists.pop(index)
        while True:
            if len(lists) == 0:
                break
            min_index = -1
            min_val = float('inf')
            for i,node in enumerate(lists):
                if min_val > node.val:
                    min_val = node.val
                    min_index = i
            print(min_val)
            temp.next = ListNode(min_val,None)
            temp = temp.next
            
            if lists[min_index].next is None:
                lists.pop(min_index)
            else:
                lists[min_index] = lists[min_index].next
        return head.next
            
