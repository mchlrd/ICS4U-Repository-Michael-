def while_factorial(n):
    result = 1
    while n > 1:
        result *= n
        n-=1
    return result


number_w = int(input("Enter a number: "))

result_while = while_factorial(number_w)

print(f"The factorial of {number_w} is {result_while}")

def for_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

number_f = int(input("Enter a number: "))

result_for = for_factorial(number_f)

print(f"The factorial of {number_f} is {result_for}")

