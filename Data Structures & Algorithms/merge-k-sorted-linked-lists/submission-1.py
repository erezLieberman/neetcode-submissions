# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge_two_lists(self,l1, l2):
                if not l1:
                    return l2
                if not l2:
                    return l1

                dummy = ListNode()
                tail = dummy

                while l1 and l2:
                    if l1.val < l2.val:
                        tail.next = l1
                        l1 = l1.next
                    else:
                        tail.next = l2
                        l2 = l2.next
                    tail = tail.next
                
                if l1:
                    tail.next = l1
                if l2:
                    tail.next = l2

                return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return 

        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            temp_res = []
            for i in range(0,len(lists),2):
                if i == len(lists) -1 :
                    temp_res.append(lists[i])
                else:
                    temp_res.append(self.merge_two_lists(lists[i], lists[i+1]))
            lists = temp_res
        return lists[0]
        


      
            

        