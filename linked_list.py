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


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()
