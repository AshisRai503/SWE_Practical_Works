# Define Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList Class with All Methods
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # New Method: Find the middle element
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    # New Method: Detect if the list has a cycle
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # New Method: Remove duplicates from an unsorted linked list
    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()
        current = self.head
        seen.add(current.data)
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next  # Remove duplicate
            else:
                seen.add(current.next.data)
                current = current.next

    # New Method: Merge two sorted linked lists into a single sorted linked list
    def merge_sorted(self, other_list):
        dummy = Node(0)
        tail = dummy
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        # Append the remaining nodes
        tail.next = current1 if current1 else current2

        # Set the head to the merged list's head
        self.head = dummy.next

# Test the LinkedList
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.display()  # Output: 1 -> 2 -> 3 -> 3 -> 4

# Test find_middle
print("Middle element:", ll.find_middle())  # Output: Middle element: 3

# Test remove_duplicates
ll.remove_duplicates()
ll.display()  # Output: 1 -> 2 -> 3 -> 4

# Create another sorted linked list and merge
ll2 = LinkedList()
ll2.append(1)
ll2.append(3)
ll2.append(5)
ll2.display()  # Output: 1 -> 3 -> 5

# Merge ll2 into ll
ll.merge_sorted(ll2)
ll.display()  # Output: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5

# Test for cycle detection
print("Has cycle:", ll.has_cycle())  # Output: Has cycle: False
# Creating a cycle for testing
ll.head.next.next.next.next = ll.head.next
print("Has cycle:", ll.has_cycle())  # Output: Has cycle: True
