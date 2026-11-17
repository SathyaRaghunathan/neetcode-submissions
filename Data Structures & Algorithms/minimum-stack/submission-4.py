class MinStack:

    def __init__(self):
        self.s1 = []
        self.ms = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if self.ms:
            self.ms.append( min(val,self.ms[-1]) )
        else:
            self.ms.append(val)

    def pop(self) -> None:
        self.s1.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.ms[-1]
