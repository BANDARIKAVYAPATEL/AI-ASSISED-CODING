def count_vowels(text):
    """
    Count the number of vowels in a given string.
    
    Vowels are: a, e, i, o, u (case-insensitive)
    
    Args:
        text (str): The string to analyze
        
    Returns:
        int: The number of vowels found
    """
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count


# Alternative version using sum and list comprehension
def count_vowels_compact(text):
    """Count vowels using a more compact approach."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


# Main program
if __name__ == "__main__":
    print("Vowel Counter")
    print("=" * 50)
    
    # Get input from user
    user_input = input("Enter a string: ")
    vowel_count = count_vowels(user_input)
    print(f"\nNumber of vowels: {vowel_count}")
    
    # Test cases
    print("\n" + "=" * 50)
    print("Test Cases:")
    print("=" * 50)
    
    test_strings = [
        "Hello World",
        "Programming",
        "Python",
        "aeiou",
        "bcdfg",
        "The quick brown fox jumps over the lazy dog"
    ]
    
    for text in test_strings:
        count = count_vowels(text)
        print(f'"{text}" → {count} vowels')
