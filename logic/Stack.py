class Stack:
    def __init__(self):
        self.my_list = list()
    def push(self, x):
        self.my_list.append(x)
    def pop(self):
        return self.my_list.pop()