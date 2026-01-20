import math


def classify_number(num):
    """
    Classify a number as Prime, Composite, or Neither.
    
    Constraints handled:
    - Input validation
    - Negative number handling
    - Optimized algorithm for efficiency
    - Meaningful messages
    
    Args:
        num (int): The number to classify
        
    Returns:
        str: Classification message with details
    """
    # Input validation
    try:
        num = int(num)
    except (ValueError, TypeError):
        return "Invalid Input: Please provide a valid integer"
    
    # Handle negative numbers
    if num < 0:
        return f"{num} is Neither (negative numbers are not classified as Prime or Composite)"
    
    # Handle special cases: 0 and 1
    if num == 0:
        return "0 is Neither (0 is not classified as Prime or Composite)"
    
    if num == 1:
        return "1 is Neither (1 is not considered Prime or Composite)"
    
    # Handle 2 (the only even prime)
    if num == 2:
        return f"{num} is Prime"
    
    # Even numbers greater than 2 are composite
    if num % 2 == 0:
        return f"{num} is Composite (divisible by 2)"
    
    # Check for odd divisors up to sqrt(num)
    sqrt_num = int(math.sqrt(num))
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return f"{num} is Composite (divisible by {i})"
    
    # If no divisors found, it's prime
    return f"{num} is Prime"


def is_prime(num):
    """
    Check if a number is prime (returns boolean).
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if not isinstance(num, int) or num < 2:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    sqrt_num = int(math.sqrt(num))
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return False
    
    return True


# Test cases and demonstrations
if __name__ == "__main__":
    print("=" * 70)
    print("NUMBER CLASSIFICATION: Prime, Composite, or Neither")
    print("=" * 70)
    
    # Test cases
    test_numbers = [-5, 0, 1, 2, 3, 4, 5, 10, 11, 15, 17, 20, 29, 30, 97, 100]
    
    print("\nClassification Results:\n")
    print(f"{'Number':<10} {'Classification':<60}")
    print("-" * 70)
    
    for num in test_numbers:
        result = classify_number(num)
        print(f"{num:<10} {result}")
    
    # Performance demonstration
    print("\n" + "=" * 70)
    print("Performance Test - Large Numbers:")
    print("=" * 70 + "\n")
    
    large_numbers = [1000000007, 1000000008, 1000000009, 9999991]
    
    for num in large_numbers:
        result = classify_number(num)
        print(result)
    
    # Additional test with invalid input
    print("\n" + "=" * 70)
    print("Input Validation Test:")
    print("=" * 70 + "\n")
    
    invalid_inputs = ["abc", 3.14, None]
    
    for inp in invalid_inputs:
        result = classify_number(inp)
        print(f"Input: {repr(inp)} -> {result}")
    
    # Boolean check function demo
    print("\n" + "=" * 70)
    print("Prime Check (Boolean Output):")
    print("=" * 70 + "\n")
    
    check_numbers = [2, 17, 25, 97]
    for num in check_numbers:
        print(f"is_prime({num}): {is_prime(num)}")
