def compute_even_odd_statistics(numbers):
    """
    Compute comprehensive statistics for even and odd numbers in a collection.
    
    This function efficiently calculates sums and counts for even and odd numbers
    using Python generator expressions, which minimizes memory overhead and 
    provides optimal performance for large datasets.
    
    Args:
        numbers (list, tuple, or iterable): Collection of numeric values to analyze.
                                           Must contain valid numeric types (int, float).
    
    Returns:
        dict: Dictionary containing the following keys:
            - 'even_sum' (numeric): Sum of all even numbers
            - 'odd_sum' (numeric): Sum of all odd numbers
            - 'total_sum' (numeric): Combined sum of all numbers
            - 'even_count' (int): Count of even numbers
            - 'odd_count' (int): Count of odd numbers
            - 'total_count' (int): Total count of numbers
    
    Raises:
        TypeError: If input is None or not iterable
        ValueError: If the collection is empty
    
    Examples:
        >>> stats = compute_even_odd_statistics([1, 2, 3, 4, 5])
        >>> stats['even_sum']
        6
        >>> stats['odd_sum']
        9
    """
    # Input validation
    if numbers is None:
        raise TypeError("Input cannot be None")
    
    try:
        # Convert to list to allow multiple iterations
        numbers_list = list(numbers)
    except TypeError:
        raise TypeError("Input must be an iterable collection of numbers")
    
    if not numbers_list:
        raise ValueError("Input collection cannot be empty")
    
    # Calculate sums using generator expressions for memory efficiency
    even_sum = sum(num for num in numbers_list if num % 2 == 0)
    odd_sum = sum(num for num in numbers_list if num % 2 != 0)
    
    # Calculate counts using generator expressions
    even_count = sum(1 for num in numbers_list if num % 2 == 0)
    odd_count = sum(1 for num in numbers_list if num % 2 != 0)
    
    return {
        'even_sum': even_sum,
        'odd_sum': odd_sum,
        'total_sum': even_sum + odd_sum,
        'even_count': even_count,
        'odd_count': odd_count,
        'total_count': len(numbers_list)
    }


def display_statistics_report(numbers):
    """
    Generate and display a formatted statistical report for even and odd numbers.
    
    This function computes statistics and presents them in a clean, readable format
    suitable for console output and logging.
    
    Args:
        numbers (list, tuple, or iterable): Collection of numeric values to analyze.
    
    Returns:
        dict: The statistics dictionary from compute_even_odd_statistics()
    
    Raises:
        TypeError: If input is None or not iterable
        ValueError: If the collection is empty
    
    Note:
        This function will print output to console. Use compute_even_odd_statistics()
        directly if only the data is needed without console output.
    """
    # Compute statistics with error handling
    result = compute_even_odd_statistics(numbers)
    
    # Display formatted report
    print(f"Input List: {list(numbers)}")
    print(f"Even Sum: {result['even_sum']:>10} (Count: {result['even_count']})")
    print(f"Odd Sum:  {result['odd_sum']:>10} (Count: {result['odd_count']})")
    print(f"Total Sum: {result['total_sum']:>9} (Total: {result['total_count']} numbers)")
    print("-" * 50)
    
    return result


def compute_statistics_for_range(start, end):
    """
    Compute even and odd statistics for a numeric range.
    
    This is a convenience function that generates a range of consecutive integers
    and computes statistics on them.
    
    Args:
        start (int): Starting value of the range (inclusive)
        end (int): Ending value of the range (inclusive)
    
    Returns:
        dict: Statistics dictionary from compute_even_odd_statistics()
    
    Raises:
        TypeError: If start or end are not integers
        ValueError: If start > end
    
    Examples:
        >>> stats = compute_statistics_for_range(1, 10)
        >>> stats['even_sum']
        30
    """
    # Input validation
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both start and end must be integers")
    
    if start > end:
        raise ValueError("start must be less than or equal to end")
    
    # Generate range and compute statistics
    numbers = list(range(start, end + 1))
    return compute_even_odd_statistics(numbers)


# Main execution block - demonstrates module functionality
if __name__ == "__main__":
    """
    Main execution block demonstrating the even/odd statistics computation module.
    
    This block demonstrates:
    1. Computing statistics from custom lists
    2. Computing statistics from numeric ranges
    3. Handling lists with negative numbers
    4. Interactive user input with error handling
    """
    
    print("=" * 50)
    print("Even and Odd Statistics Calculator")
    print("Production Version 1.0")
    print("=" * 50)
    
    # Example 1: Basic list of numbers 1-10
    print("\n[Example 1] Basic List (1-10)")
    numbers_example_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    display_statistics_report(numbers_example_1)
    
    # Example 2: Custom mixed numbers
    print("[Example 2] Custom Mixed Numbers")
    numbers_example_2 = [15, 22, 33, 44, 55, 66, 77, 88, 99]
    display_statistics_report(numbers_example_2)
    
    # Example 3: Using range-based computation
    print("[Example 3] Range-Based (1-20)")
    result_example_3 = compute_statistics_for_range(1, 20)
    print(f"Range: 1 to 20")
    print(f"Even Sum: {result_example_3['even_sum']:>10} (Count: {result_example_3['even_count']})")
    print(f"Odd Sum:  {result_example_3['odd_sum']:>10} (Count: {result_example_3['odd_count']})")
    print(f"Total Sum: {result_example_3['total_sum']:>9} (Total: {result_example_3['total_count']} numbers)")
    print("-" * 50)
    
    # Example 4: List containing negative numbers
    print("\n[Example 4] List with Negative Numbers")
    numbers_example_4 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    display_statistics_report(numbers_example_4)
    
    # Interactive user input mode
    print("[Interactive Mode] Enter Custom Data")
    user_input = input("Enter numbers separated by spaces (press Enter to skip): ").strip()
    
    if user_input:
        try:
            # Parse user input and compute statistics
            user_numbers = list(map(int, user_input.split()))
            
            # Validate that we have valid numbers
            if not user_numbers:
                print("Error: No valid numbers entered.")
            else:
                print("\nYour Input Analysis:")
                display_statistics_report(user_numbers)
                
        except ValueError as e:
            print(f"Error: Invalid input. Please enter only integers separated by spaces.")
            print(f"Details: {str(e)}")
