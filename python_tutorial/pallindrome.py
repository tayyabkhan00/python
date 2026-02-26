# Method 1: Simple (Using String Reverse)
# Take input from user
text = input("Enter a word or number: ")

# Reverse the string
reverse_text = text[::-1]

# Check palindrome
if text == reverse_text:
    print("It is a palindrome ✅")
else:
    print("It is not a palindrome ❌")

# Method 2: Without Using Slicing (Beginner Friendly Logic)
text = input("Enter a word or number: ")

reverse_text = ""

for char in text:
    reverse_text = char + reverse_text

if text == reverse_text:
    print("It is a palindrome ✅")
else:
    print("It is not a palindrome ❌")

# Using Mathematical Logic (Best for Practice)
num = int(input("Enter a number: "))

original_num = num
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

if original_num == reverse_num:
    print("It is a palindrome number ✅")
else:
    print("It is not a palindrome number ❌")

# Method 2: Simple (Convert to String)
num = input("Enter a number: ")

if num == num[::-1]:
    print("It is a palindrome number ✅")
else:
    print("It is not a palindrome number ❌")