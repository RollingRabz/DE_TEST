def reverse_num(num: int):
    if num < 0:
        # Check if number is positive
        raise ValueError("Input must be a non-negative integer.") 
    
    ans = 0                           # variable to store answer
    while num > 0:                    # repeat until number is 0 which mean no number to reverse anymore
        last_digit = num % 10         # Get the last digit
        ans = ans * 10 + last_digit   # Append the digit
        num //= 10                    # Remove the last digit
    
    return ans

# Run this file for test
assert reverse_num(1234) == 4321
assert reverse_num(20903) == 30902
assert reverse_num(1_000_234) == 4320001
assert reverse_num(4444) == 4444
assert reverse_num(1) == 1
assert reverse_num(0) == 0