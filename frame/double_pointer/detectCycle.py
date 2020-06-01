
def detectCycle(head):
    fast,slow = head,head

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow :break
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow