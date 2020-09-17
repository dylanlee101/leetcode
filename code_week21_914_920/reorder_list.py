'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:  # 节点为空或1个，直接返回
            return head
        end, slow, fast = head, head, head
        while fast and fast.next:  # 查找中点，偶数长度时为靠右节点
            end = slow
            slow = slow.next
            fast = fast.next.next
        end.next = None

        pre, cur = None, slow

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        first, second = head, pre

        while first.next and second.next:
            temp2 = first.next
            first.next = second
            temp3 = second.next
            second.next = temp2
            first = temp2
            second = temp3

        if not first.next:
            first.next = second

        return head