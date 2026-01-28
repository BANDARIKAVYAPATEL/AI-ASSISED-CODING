def count_lines(filename):
    """
    Count the number of lines in a text file.
    
    Args:
        filename (str): The path to the text file
        
    Returns:
        int: The number of lines in the file, or -1 if file not found
    """
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
    except Exception as e:
        print(f"Error reading file: {e}")
        return -1


# Alternative version using readlines()
def count_lines_v2(filename):
    """Count lines using readlines() method."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
    except Exception as e:
        print(f"Error reading file: {e}")
        return -1


# Main program
if __name__ == "__main__":
    print("Text File Line Counter")
    print("=" * 50)
    
    # Test with sample file
    print("\nTest 1: Using sample.txt")
    print("-" * 50)
    sample_file = "sample.txt"
    line_count = count_lines(sample_file)
    if line_count != -1:
        print(f"Number of lines in '{sample_file}': {line_count}")
    
    # Get filename from user (optional)
    print("\n" + "=" * 50)
    user_file = input("Enter another filename to count (or press Enter to skip): ")
    if user_file.strip():
        line_count = count_lines(user_file)
        if line_count != -1:
            print(f"Number of lines in '{user_file}': {line_count}")
