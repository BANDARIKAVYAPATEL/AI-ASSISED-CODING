def check_even_or_odd(num):
    """
    Check whether a number is even or odd with validation.
    
    Args:
        num: The value to check (can be int, string, or other type)
        
    Returns:
        str: "Even" or "Odd" if valid, error message otherwise
    """
    # Input validation
    try:
        # Convert to integer if it's a string
        if isinstance(num, str):
            num = int(num.strip())
        elif not isinstance(num, int):
            # Try to convert other types to int
            num = int(num)
    except (ValueError, TypeError):
        return "Invalid Input: Please provide a valid integer"
    
    # Check if number is even or odd
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_even_or_odd_verbose(num):
    """
    Check whether a number is even or odd with detailed output.
    
    Args:
        num: The value to check
        
    Returns:
        dict: Dictionary with classification and details
    """
    try:
        if isinstance(num, str):
            num = int(num.strip())
        elif not isinstance(num, int):
            num = int(num)
    except (ValueError, TypeError):
        return {
            "valid": False,
            "message": "Invalid Input: Please provide a valid integer",
            "number": None,
            "classification": None
        }
    
    is_even = num % 2 == 0
    classification = "Even" if is_even else "Odd"
    
    return {
        "valid": True,
        "number": num,
        "classification": classification,
        "message": f"{num} is {classification}",
        "divisible_by_2": is_even,
        "remainder": num % 2
    }


def is_even(num):
    """
    Check if a number is even (returns boolean).
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if even, False otherwise
    """
    try:
        if isinstance(num, str):
            num = int(num.strip())
        return num % 2 == 0
    except (ValueError, TypeError):
        return None


def is_odd(num):
    """
    Check if a number is odd (returns boolean).
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if odd, False otherwise
    """
    try:
        if isinstance(num, str):
            num = int(num.strip())
        return num % 2 != 0
    except (ValueError, TypeError):
        return None


# Interactive mode and demonstrations
if __name__ == "__main__":
    print("=" * 70)
    print("EVEN OR ODD CHECKER WITH INPUT VALIDATION")
    print("=" * 70)
    
    # Examples from user request
    print("\nExamples from User Request:\n")
    examples = [8, 15, 0]
    
    for num in examples:
        result = check_even_or_odd(num)
        print(f"Input: {num} -> Output: {result}")
    
    # Test cases with various inputs
    print("\n" + "=" * 70)
    print("Test Cases - Valid Inputs:")
    print("=" * 70 + "\n")
    
    test_cases = [-10, -5, -1, 0, 1, 2, 3, 5, 10, 100, 999, 1000]
    
    print(f"{'Number':<10} {'Classification':<20} {'Divisible by 2':<20}")
    print("-" * 70)
    
    for num in test_cases:
        result = check_even_or_odd(num)
        divisible = "Yes" if num % 2 == 0 else "No"
        print(f"{num:<10} {result:<20} {divisible:<20}")
    
    # Input validation tests
    print("\n" + "=" * 70)
    print("Input Validation Tests:")
    print("=" * 70 + "\n")
    
    invalid_inputs = ["abc", "12.5", "", "10a", None, 3.14, [], {}]
    
    print(f"{'Input':<20} {'Type':<20} {'Result':<30}")
    print("-" * 70)
    
    for inp in invalid_inputs:
        result = check_even_or_odd(inp)
        print(f"{repr(inp):<20} {type(inp).__name__:<20} {result:<30}")
    
    # String inputs that are valid
    print("\n" + "=" * 70)
    print("String Input Conversion:")
    print("=" * 70 + "\n")
    
    string_inputs = ["8", "15", "  42  ", "-7", "0"]
    
    for inp in string_inputs:
        result = check_even_or_odd(inp)
        print(f"Input: {repr(inp)} -> Output: {result}")
    
    # Boolean functions demo
    print("\n" + "=" * 70)
    print("Boolean Functions Demo:")
    print("=" * 70 + "\n")
    
    test_nums = [4, 7, 0, -3, 100]
    
    print(f"{'Number':<10} {'is_even()':<15} {'is_odd()':<15}")
    print("-" * 70)
    
    for num in test_nums:
        print(f"{num:<10} {str(is_even(num)):<15} {str(is_odd(num)):<15}")
    
    # Verbose output demo
    print("\n" + "=" * 70)
    print("Detailed Information:")
    print("=" * 70 + "\n")
    
    for num in [8, 15, 0]:
        info = check_even_or_odd_verbose(num)
        if info["valid"]:
            print(f"Number: {info['number']}")
            print(f"Classification: {info['classification']}")
            print(f"Message: {info['message']}")
            print(f"Remainder when divided by 2: {info['remainder']}\n")
        else:
            print(f"Error: {info['message']}\n")
    
    # Interactive mode
    print("=" * 70)
    print("Interactive Mode:")
    print("=" * 70 + "\n")
    
    while True:
        try:
            user_input = input("Enter a number (or 'quit' to exit): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            result = check_even_or_odd(user_input)
            print(f"Output: {result}\n")
        
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            break
        except Exception as e:
            print(f"Error: {e}\n")
