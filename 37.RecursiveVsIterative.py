def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

# recursive means a function calls itself inside it
def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_iterative(6))
print(factorial_recursive(6))
