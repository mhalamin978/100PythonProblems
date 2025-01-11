# Input from user
a = int(input("Give me a number: "))

# Store the original number for comparison
original_number = a

# Reverse the number
reversed_number = 0
while a > 0:
    digit = a % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Add the digit to reversed number
    a //= 10  # Remove the last digit

# Check if the number is a palindrome
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")