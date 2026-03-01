try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Please enter a valid number!")