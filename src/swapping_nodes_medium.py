from wrappers import time_it

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def build_list(head):
    firstnode = ListNode()
    curnode = firstnode
    for h in head:
        curnode.val = h
        if head.index(h) != len(head) - 1:
            curnode.next = ListNode()
            curnode = curnode.next
        
    return firstnode

def swap_nodes(head, k):
    head_vals = []
    curnode = head
    while curnode.next != None:
        head_vals.append(curnode.val)
        curnode = curnode.next
    
    head_vals.append(curnode.val)
    
    k_r = len(head_vals) - k + 1
    v_l = head_vals[k - 1]
    v_r = head_vals[k_r - 1]
    counter = 1
    curnode = head
    while curnode is not None:
        if counter == k:
            curnode.val = v_r
        elif counter == k_r:
            curnode.val = v_l

        
        counter += 1
        curnode = curnode.next
        
    return head
    
        

def main():
    h = [1]
    head = build_list(h)
    k = 1
    ans = swap_nodes(head, k)
    
    
if __name__ == "__main__":
    main()