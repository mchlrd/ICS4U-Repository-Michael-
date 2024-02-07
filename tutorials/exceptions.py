try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))

    result = numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
#except Exception:
   # print("Something went wrong")
