from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        # self.storage = ?
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.remove_tail()
        else:
            return
