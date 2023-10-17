class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f'{"🍪"*self.size}'

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError(f"jar has a capacity of {self.capacity} and is currently holding {self.size} cookies in it\nnot enough capacity in jar to add {n} cookies")
        else:
            self.size = self.size + n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError(f"jar has a capacity of {self.capacity} and is currently holding {self.size} cookies in it\nnot enough cookies in jar to withdraw {n} cookies")
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("Negative capacity not allowed")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n=0):
        if self.capacity < n:
            raise ValueError(f'size cannot be bigger than capacity')
        else:
            self._size = n

def main():
    oreos_jar = Jar()
    oreos_jar.deposit(50)
    print(oreos_jar)

if __name__ == "__main__":
    main()
