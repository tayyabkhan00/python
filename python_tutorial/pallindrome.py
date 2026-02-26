# Take input from user
text = input("Enter a word or number: ")

# Reverse the string
reverse_text = text[::-1]

# Check palindrome
if text == reverse_text:
    print("It is a palindrome ✅")
else:
    print("It is not a palindrome ❌")