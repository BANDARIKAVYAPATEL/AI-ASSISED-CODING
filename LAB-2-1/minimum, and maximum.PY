def calculate_stats(numbers):
    """
    Calculate mean, minimum, and maximum values of a list of numbers.
    
    Args:
        numbers: A list of numeric values
    
    Returns:
        A dictionary containing mean, min, and max values
    """
    if not numbers:
        print("Error: List is empty!")
        return None
    
    mean = sum(numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    return {
        'mean': mean,
        'minimum': minimum,
        'maximum': maximum
    }


def display_stats(numbers):
    """Display the statistics for a list of numbers."""
    stats = calculate_stats(numbers)
    
    if stats:
        print(f"List of numbers: {numbers}")
        print(f"Mean: {stats['mean']:.2f}")
        print(f"Minimum: {stats['minimum']}")
        print(f"Maximum: {stats['maximum']}")


# Example usage
if __name__ == "__main__":
    # Test with sample data
    test_numbers = [10, 25, 30, 45, 50]
    display_stats(test_numbers)
    
    print("\n--- Another Example ---")
    test_numbers_2 = [5, 15, 8, 22, 12, 35]
    display_stats(test_numbers_2)
