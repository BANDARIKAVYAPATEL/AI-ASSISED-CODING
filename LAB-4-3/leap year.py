def is_leap_year(year):
    """
    Determine whether a given year is a leap year.
    
    A leap year is:
    - Divisible by 400, OR
    - Divisible by 4 AND NOT divisible by 100
    
    Args:
        year (int): The year to check
        
    Returns:
        str: A message indicating if the year is a leap year or not
    """
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"


# Main program
if __name__ == "__main__":
    print("Leap Year Checker")
    print("=" * 40)
    
    # Get year input from user
    try:
        year = int(input("Enter a year: "))
        result = is_leap_year(year)
        print(result)
    except ValueError:
        print("Please enter a valid year (integer)")
    
    # Test with multiple years
    print("\n" + "=" * 40)
    print("Test Cases:")
    print("=" * 40)
    test_years = [2000, 2004, 2024, 2023, 2100, 1900, 2400]
    
    for year in test_years:
        print(is_leap_year(year))
