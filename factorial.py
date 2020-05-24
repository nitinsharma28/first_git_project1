def get_factorial(n):
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

# can find with recurssion function
# def get_factorial_recu(n)
#     if n==1:
#         return n
#     return n*get_factorial_recu(n-1)

if __name__ == "__main__":
    n = int(input("enter the factorial no "))
    result = 1
    for item in range(1, n + 1):
        result = result * item
    print(result)
