def is_prime(n):
    # 不能包含第一个从2开始
    i = 2
    # 不能包含最后一个, 最后一个作为结尾
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def fizzbuzz(n):
    i = 1
    while i <= n:
        if i % 3 == i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        i += 1


def has_digit(n, k):
    while n >= 1:
        if n % 10 == k:
            return True
        n //= 10
    return False


def unique_digits(n):
    i = 0
    sum = 0
    while i < 10:
        if has_digit(n, i):
            sum += 1
        i += 1
    return sum
