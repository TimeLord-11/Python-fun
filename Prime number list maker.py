#prime numbers in a given range and add to a list called primes
low_num = int(input("Enter lowest #: "))
high_num = int(input("Enter highest #: "))
primes = []
for num in range(low_num,high_num+1):
    if num > 1:
        for x in range (2,num):
            if num % x == 0:
                break
        else:
            primes.append(num)   # can just print(num) here to just loop primes one line at a time
print(primes)
