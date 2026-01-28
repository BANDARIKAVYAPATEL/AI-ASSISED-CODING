def is_leap_year(year):
    """
    Check if a year is a leap year.
    A leap year is:
    - Divisible by 4 AND
    - Either not divisible by 100 OR divisible by 400
    
    Args:
        year: Integer representing the year
    
    Returns:
        Boolean: True if leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def leap_years_in_range(start_year, end_year):
    """Find all leap years in a given range."""
    leap_years = [year for year in range(start_year, end_year + 1) if is_leap_year(year)]
    return leap_years


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("Leap Year Checker")
    print("=" * 50)
    
    # Test individual years
    test_years = [2000, 1900, 2004, 2100, 2024, 2023, 2025, 1996, 2001]
    
    print("\nChecking individual years:")
    for year in test_years:
        result = is_leap_year(year)
        status = "[YES] Leap Year" if result else "[NO] Not a Leap Year"
        print(f"{year}: {status}")
    
    # Find leap years in range
    print("\n" + "=" * 50)
    print("Leap years from 2000 to 2030:")
    leap_in_range = leap_years_in_range(2000, 2030)
    print(leap_in_range)
    
    # Count leap years in a century
    print("\n" + "=" * 50)
    print("Leap years in 21st century (2000-2099):")
    leap_21st = leap_years_in_range(2000, 2099)
    print(f"Total: {len(leap_21st)} leap years")
    print(f"First 10: {leap_21st[:10]}")
    print(f"Last 10: {leap_21st[-10:]}")
    
    # Interactive check
    print("\n" + "=" * 50)
    print("Interactive Check:")
    user_input = input("Enter a year to check (or press Enter to skip): ").strip()
    
    if user_input:
        try:
            year = int(user_input)
            if is_leap_year(year):
                print(f"{year} is a Leap Year!")
            else:
                print(f"{year} is NOT a Leap Year.")
        except ValueError:
            print("Invalid input! Please enter a valid year.")
