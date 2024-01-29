from functools import cache
import time


def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:

        return n * factorial(n - 1)


@cache
def cached_factorial(n):

    if n == 0 or n == 1:
        return 1
    else:

        return n * factorial(n - 1)

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def cached_fibonacci(n):
    # Base cases: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = 10

    # ფაქტორიალი
    # start_time = time.time()
    #
    # cached_result = cached_factorial(n)
    # print(f"{n}-ის ფაქტორიალი არის: {cached_result}")
    #
    # end_time = time.time()
    # execution_time = end_time - start_time
    #
    # print(f"ქეშირებულად გამოითვალა: {execution_time} წამში")
    #
    # start_time = time.time()
    #
    # result = factorial(n)
    # print(f"{n}-ის ფაქტორიალი არის: {result}")
    # end_time = time.time()
    #
    # execution_time = end_time - start_time
    #
    # print(f"გამოითვალა: {execution_time} წამში")


    # ფიბონაჩი
    start_time = time.time()

    cached_result = cached_fibonacci(n)
    print(f"{n} წევრი ფიბონაჩის მიმდევრობაშივ არის: {cached_result}")

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"ქეშირებულად გამოითვალა: {execution_time} წამში")

    start_time = time.time()

    result = factorial(n)
    print(f"{n} წევრი ფიბონაჩის მიმდევრობაში არის: {result}")
    end_time = time.time()

    execution_time = end_time - start_time

    print(f"გამოითვალა: {execution_time} წამში")