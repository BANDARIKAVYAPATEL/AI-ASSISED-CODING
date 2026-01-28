def format_name(full_name):
    """
    Format a full name as "Last, First".
    
    Args:
        full_name (str): The full name in "First Last" format
        
    Returns:
        str: The name formatted as "Last, First"
    """
    parts = full_name.strip().split()
    
    if len(parts) < 2:
        return full_name  # Return as-is if only one part
    
    first_name = parts[0]
    last_name = parts[-1]
    
    return f"{last_name}, {first_name}"


# Main program
if __name__ == "__main__":
    print("Name Formatter - 'First Last' to 'Last, First'")
    print("=" * 50)
    
    # Get input from user
    name_input = input("Enter a full name: ")
    formatted = format_name(name_input)
    print(f"Formatted: {formatted}")
    
    # Test cases
    print("\n" + "=" * 50)
    print("Test Cases:")
    print("=" * 50)
    
    test_names = [
        "John Smith",
        "Anita Rao",
        "Mary Jane Watson",
        "Michael Scott"
    ]
    
    for name in test_names:
        print(f'"{name}" → "{format_name(name)}"')
