def fatorial(n):
    return n * (fatorial(n - 1) if (n - 1) > 1 else 1)


print(f'10! = {fatorial(10)}')