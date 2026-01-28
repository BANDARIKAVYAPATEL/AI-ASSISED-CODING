def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 400, OR
    - It is divisible by 4 AND NOT divisible by 100
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Alternative concise version
def is_leap_year_concise(year):
    """Concise version using a single boolean expression."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


# Test cases
if __name__ == "__main__":
    test_years = [2000, 2004, 2100, 2024, 2023, 1900, 2400]
    
    print("Leap Year Checker:")
    print("-" * 40)
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year}: {'Leap Year' if result else 'Not a Leap Year'}")
