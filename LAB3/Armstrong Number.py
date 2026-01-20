def is_armstrong_number(num):
    """
    Check whether a given number is an Armstrong number.
    
    An Armstrong number (narcissistic number) is a number that is equal to 
    the sum of its own digits each raised to the power of the number of digits.
    
    Examples:
        153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
        370 = 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370
    
    Args:
        num (int): The number to check
        
    Returns:
        str: "Armstrong Number" if it is an Armstrong number, 
             "Not an Armstrong Number" otherwise
    """
    # Convert to string to work with individual digits
    num_str = str(abs(num))  # Use abs to handle negative numbers
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    if sum_of_powers == abs(num):
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"


def is_armstrong_bool(num):
    """
    Check whether a given number is an Armstrong number (returns boolean).
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if it is an Armstrong number, False otherwise
    """
    num_str = str(abs(num))
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == abs(num)


# Test cases
if __name__ == "__main__":
    test_cases = [153, 370, 371, 407, 123, 100, 9, 10, 1, 0]
    
    print("Armstrong Number Checker:\n")
    print(f"{'Number':<10} {'Result':<30} {'Calculation':<40}")
    print("-" * 80)
    
    for num in test_cases:
        num_str = str(num)
        num_digits = len(num_str)
        sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
        result = is_armstrong_number(num)
        
        # Show calculation
        calculation = " + ".join([f"{digit}^{num_digits}" for digit in num_str])
        print(f"{num:<10} {result:<30} {calculation} = {sum_of_powers}")
    
    print("\n" + "=" * 80)
    print("Examples from user request:\n")
    print(f"Input: 153 -> Output: {is_armstrong_number(153)}")
    print(f"Input: 370 -> Output: {is_armstrong_number(370)}")
    print(f"Input: 123 -> Output: {is_armstrong_number(123)}")
