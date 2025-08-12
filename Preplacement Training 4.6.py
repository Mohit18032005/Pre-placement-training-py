int josephus(int n, int k) {
    if (n == 1)
        return 1;
    else
        return (josephus(n - 1, k) + k - 1) % n + 1;
}
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)
        
        if head is None:
            new_node.next = new_node
            return new_node
        
        curr = head
        
        if data <= head.data:
            while curr.next != head:
                curr = curr.next
            curr.next = new_node
