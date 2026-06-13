class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # ptr -> idx
        nodes = {}

        curr = head
        curr_idx = 0
        while curr:
            nodes[curr] = curr_idx
            curr = curr.next
            curr_idx += 1

        # idx -> (rand_idx, value)
        rand_map = {}

        curr = head
        idx = 0
        while curr:
            rand_idx = None if not curr.random else nodes[curr.random]
            rand_map[idx] = (rand_idx, curr.val)

            curr = curr.next
            idx += 1

        # Copy nodes
        nodes = {}

        dummy = curr = Node(0)

        for idx in range(curr_idx):
            curr.next = Node(rand_map[idx][1])
            nodes[idx] = curr.next
            curr = curr.next

        head = dummy.next

        # Restore random pointers
        curr = head
        idx = 0

        while curr:
            rand_idx = rand_map[idx][0]

            if rand_idx is not None:
                curr.random = nodes[rand_idx]

            curr = curr.next
            idx += 1

        return head