class Queue:
    def __init__(self):
        self.qu = []

    def add(self, val):
        self.qu.append(val)

    def remove(self):
        if len(self.qu) > 0:
            ele = self.qu[0]
            self.qu = self.qu[1:]
            return ele

    def peek(self):
        if len(self.qu) > 0:
            return self.qu[0]

    def isEmpty(self):
        return True if (len(self.qu) == 0) else False

