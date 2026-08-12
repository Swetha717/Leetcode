class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create duplicate nodes and interweave them
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
            
        # Step 2: Assign random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Step 3: Separate the interweaved list into two lists
        curr = head
        copy_head = head.next
        while curr:
            copy_node = curr.next
            curr.next = copy_node.next
            if copy_node.next:
                copy_node.next = copy_node.next.next
            curr = curr.next
            
        return copy_head