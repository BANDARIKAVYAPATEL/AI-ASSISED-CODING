def is_palindrome(num):
    """
    Check whether a given number is a palindrome or not.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    if num < 0:
        return False
    
    # Convert to string and check if it's the same as its reverse
    num_str = str(num)
    return num_str == num_str[::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [121, 123, 10, 0, -121, 1001, 1234, 9, 12321]
    
    for num in test_cases:
        result = is_palindrome(num)
        print(f"{num}: {result}")
