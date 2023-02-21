class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        if new_node.data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next and new_node.data > curr_node.next.data:
            curr_node = curr_node.next
        new_node.next = curr_node.next
        curr_node.next = new_node

    def merge_sorted_lists(self, llist2):
        merged_list = LinkedList()
        current_node1 = self.head
        current_node2 = llist2.head

        while current_node1 and current_node2:
            if current_node1.data < current_node2.data:
                merged_list.append(current_node1.data)
                current_node1 = current_node1.next
            else:
                merged_list.append(current_node2.data)
                current_node2 = current_node2.next

        while current_node1:
            merged_list.append(current_node1.data)
            current_node1 = current_node1.next

        while current_node2:
            merged_list.append(current_node2.data)
            current_node2 = current_node2.next

        return merged_list

list1 = LinkedList()
print("Enter elements of first linked list in ascending order separated by spaces:")
data = input().split()
for num in data:
    list1.append(int(num))

list2 = LinkedList()
print("Enter elements of second linked list in ascending order separated by spaces:")
data = input().split()
for num in data:
    list2.append(int(num))

sorted_list = list1.merge_sorted_lists(list2)

current_node = sorted_list.head
while current_node:
    print(current_node.data, end="->")
    current_node = current_node.next




