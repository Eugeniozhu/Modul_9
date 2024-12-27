import math

def is_prime(func):

    def wrapper(*args):
        func(*args)
        i = sum(args)
        factorial_ = math.factorial(i - 1)
        if (factorial_ + 1) % i == 0:
            print("Простое число")
            return i
        else:
            print("Составное")
            return i
    return wrapper


@is_prime
def sum_three(a, b, c):
    # print(f'Выполняемая функция с агументами: {a}, {b}, {c}!')
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
