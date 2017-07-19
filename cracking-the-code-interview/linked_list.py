class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        max_iteration = 100
        curr = self
        out = []
        while curr and max_iteration:
            out.append(str(curr.value))
            curr = curr.next
            max_iteration -= 1
        return ' -> '.join(out)

    def __repr__(self):
        return str(self)

    # def __eq__(self, other):
    #     return str(self) == str(other)

