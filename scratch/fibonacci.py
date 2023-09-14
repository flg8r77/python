def main():
    print(list(fibonacci(10)))

def fibonacci(n):    
    a , b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    main()