def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Factorial of n (denoted as n!) is the product of all positive integers 
    less than or equal to n.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


# Alternative recursive approach
def factorial_recursive(n):
    """
    Calculate the factorial of a given number using recursion.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


# Test cases
if __name__ == "__main__":
    test_cases = [0, 1, 5, 10, 15]
    
    print("Iterative Approach:")
    for num in test_cases:
        result = factorial(num)
        print(f"factorial({num}) = {result}")
    
    print("\nRecursive Approach:")
    for num in test_cases:
        result = factorial_recursive(num)
        print(f"factorial_recursive({num}) = {result}")
    
    # Example from user request
    print(f"\nExample: factorial(5) = {factorial(5)}")
