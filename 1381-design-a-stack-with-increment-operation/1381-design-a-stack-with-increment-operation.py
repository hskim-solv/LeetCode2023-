class CustomStack:

    def __init__(self, maxSize: int):
        self.ms = maxSize
        self.box = []
    def push(self, x: int) -> None:
        if len(self.box) < self.ms:
            self.box.append(x)
        

    def pop(self) -> int:
        if self.box:
            return self.box.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.box)) ):
            self.box[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)