import sys
import math


def main():
    n = int(input())
    if n > 1000000:
        print(round(1 / math.log(n),2))
        return
    primes = [5, 7, 11, 13]
    fast = 1
    i = 17
    step = 2
    while i <= n:
        for j in primes:
            if i % j == 0:
                #print (f'{i} - составное ', end ='\t')
                break
            if j >= int(i ** (0.5)):
                primes.append(i)
                #print(f'{i} - простое ', end='\t')
                break
        fast = 1 - fast
        step = step + 2 + 2 * fast
        #print(f'fast = {fast}, step = {step}, change = {2 + 2 * fast};', end = '\t')
        if step % 10 == 0:
            i = i + 6
            step = i % 5
            #print(f'Следущее число {i - 2 - 2 * (1 - fast)} - делится на 5 его пропускаем, идем в {i}')
            fast = 1 - fast
        else:
            i = i + 2 + 2 * fast
            #print(f'next -> {i}')
    num = str((len(primes) + 2) / n)
    if len(num) < 4:
        num += '0' * (4 - len(num))
    print(num[:4])



if __name__ == '__main__':
    main()