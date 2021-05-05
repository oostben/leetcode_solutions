# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        temp = head
        while temp.next is not None:
            temp = temp.next
            length += 1
        length += 1
        if length < k:
            return head
        pointers =[]
        for i in range(k):
            temp = head
            for j in range(i):
                temp = temp.next
            pointers.append(temp)
        head = pointers[len(pointers)-1]
        for x in range(length // k):
            print_lis(head)
            if pointers[len(pointers)-1].next is not None:
                pointers[0].next = pointers[len(pointers)-1].next
            for idx, ptr in enumerate(pointers):
                if idx == 0: continue
                pointers[idx].next = pointers[idx-1]
            if x > 0:
                temp.next = pointers[len(pointers)-1]
            elif x == 0:
                if k == length:
                    pointers[0].next = None
            if x == (length // k) - 1:
                if length % k ==0:
                    pointers[0].next = None
            print_lis(head)
            temp = pointers[0]
            if x == (length // k) -1: break
            else:
                for i in range(len(pointers)):
                    for j in range(k):
                        pointers[i] = pointers[i].next
                pointers.reverse()
        return head
    
def print_lis(head):
    while head.next is not None:
        print(head.val, end="->")
        head = head.next
    print(head.val, end="")
    print()
        
