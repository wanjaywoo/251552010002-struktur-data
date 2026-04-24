class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_after_node (prev_node, data):
    if not prev_node:
        print("node sebelumnya tidak boleh none")
        return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

head = Node("nabhan")
head = insert_at_beginning(head,"rizwan")
head = insert_at_end(head,"yahya")

def print_linked_list(head):
    while head:
        print(f"[{head.data}]->", end="")
        head = head.next
    print("Null")
    current = head
    while current and current.data !="nabhan":
        current = current.next
    insert_after_node(current, "RIZWAN")

print_linked_list(head)
