class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return None

    def pushback(self, n: int) -> None:
        if self.size == self.getCapacity():
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        return None

    def popback(self) -> int:
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        self.arr.extend([None] * self.getCapacity())
        return None

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.arr)