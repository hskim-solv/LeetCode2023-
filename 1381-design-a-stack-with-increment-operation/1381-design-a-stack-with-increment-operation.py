class CustomStack:

    def __init__(self, maxSize: int):
        self.ms = maxSize
        self.box = []
        self.cl = 0
    def push(self, x: int) -> None:
        if self.cl < self.ms:
            self.cl += 1
            self.box.append(x)
        

    def pop(self) -> int:
        if self.box:
            self.cl -= 1
            return self.box.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,self.cl) ):
            self.box[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)