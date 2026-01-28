def is_armstrong(num):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is equal to the sum of its digits each raised 
    to the power of the number of digits.
    
    Args:
        num: Integer to check
    
    Returns:
        Boolean: True if Armstrong number, False otherwise
    """
    # Convert to string to get number of digits
    num_str = str(abs(num))
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if it equals the original number
    return sum_of_powers == abs(num)


def check_armstrong_range(start, end):
    """Find all Armstrong numbers in a given range."""
    armstrong_numbers = [n for n in range(start, end + 1) if is_armstrong(n)]
    return armstrong_numbers


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("Armstrong Number Checker")
    print("=" * 50)
    
    # Test individual numbers
    test_numbers = [153, 370, 371, 407, 1634, 8208, 9474, 100, 123, 9]
    
    print("\nChecking individual numbers:")
    for num in test_numbers:
        result = is_armstrong(num)
        status = "[YES] Armstrong Number" if result else "[NO] Not Armstrong"
        print(f"{num}: {status}")
    
    # Find Armstrong numbers in range
    print("\n" + "=" * 50)
    print("Armstrong numbers from 1 to 1000:")
    armstrong_in_range = check_armstrong_range(1, 1000)
    print(armstrong_in_range)
    
    # Interactive check
    print("\n" + "=" * 50)
    print("Interactive Check:")
    user_input = input("Enter a number to check (or press Enter to skip): ").strip()
    
    if user_input:
        try:
            number = int(user_input)
            if is_armstrong(number):
                print(f"{number} is an Armstrong Number!")
            else:
                print(f"{number} is NOT an Armstrong Number.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
