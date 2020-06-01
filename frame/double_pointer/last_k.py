
def lastk(head,k):
    slow,fast = head,head
    while k > 0:
        fast = fast.next
        k -= 1
    while fast != None:
        slow = slow.next
        fast = fast.next

    return slow
