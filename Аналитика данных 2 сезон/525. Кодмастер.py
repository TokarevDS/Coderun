import sys


def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    i = 1
    numbers.sort(reverse=True)
    while i <= n:
        #print(f'start i = {i}')
        if numbers[i - 1] >= i**2:
            #print(f'next step {numbers[i - 1]} >= {i ** 2}')
            i += 1
        else:
            #print(f'end i = {i}')
            break
    print(i - 1)


if __name__ == '__main__':
    main()