class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    """ Merge two sorted linked lists and return it as a sorted list.
    The list should be made by splicing together the nodes of the first two lists.
    """

    if not l1 and not l2:
        return None

    merged_list = ListNode()
    current = merged_list

    while l1 != None or l2 != None:

        if not l1:
            current.next = l2
            break

        if not l2:
            current.next = l1
            break

        if l1.val <= l2.val:
            current.next = ListNode(l1.val)
            l1 = l1.next
        else:
            # add to merged list
            current.next = ListNode(l2.val)
            l2 = l2.next
        current = current.next

    return merged_list.next


def hasCycle(head):
    """Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false."""

    if not head:
        return False

    fast_node = head.next
    slow_node = head

    while fast_node != None and fast_node.next != None:
        if fast_node == slow_node:
            return True
        fast_node = fast_node.next.next
        slow_node = slow_node.next
    return False


def removeElements(head, val):
    """"Remove all elements from a linked list of integers that have value val."""

    if not head:
        return

    while head and head.val == val:
        head = head.next

    current = head

    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return head


class Solution:
    def deleteNode(self, node):
        """ Write a function to delete a node in a singly-linked list.
        You will not be given access to the head of the list,
        instead you will be given access to the node to be deleted directly.
        It is guaranteed that the node to be deleted is not a tail node in the list.
        """

        node.val = node.next.val
        node.next = node.next.next


def reverseList(head):
    """Reverse a singly linked list."""

    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev


def mergeInBetween(list1, a, b, list2):
    """You are given two linked lists: list1 and list2 of sizes n and m respectively.

        Remove list1's nodes from the ath node to the bth node, and put list2 in their place."""

    end = list1
    for i in range(b + 1):
        end = end.next

    templ2 = list2

    while templ2 and templ2.next:
        templ2 = templ2.next

    templ2.next = end

    beginning = list1
    for i in range(a - 1):
        beginning = beginning.next

    beginning.next = list2

    return list1
