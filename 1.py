import sys
def main():
    a, b, c = map(int, input().split())
    numbers = [a, b, c]
    numbers.sort()
    print(numbers[1])
if __name__ == '__main__':
    main()
