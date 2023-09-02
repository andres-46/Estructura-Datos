def factorial (n):
    if n == 1:
        return 1
    return n * factorial(n-1)

resul = factorial(5)
print(f"Factorial de 5 es: {resul}")
