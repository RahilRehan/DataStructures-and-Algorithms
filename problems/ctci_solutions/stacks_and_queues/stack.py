class Stack:
    def __init__(self):
        self.st = []

    def push(self, val):
        self.st.append(val)

    def pop(self):
        if len(self.st)>0: return self.st.pop()

    def peek(self):
        if len(self.st)>0: return self.st[-1]

    def isEmpty(self):
        return True if(len(self.st)==0) else False
