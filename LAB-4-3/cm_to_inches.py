def cm_to_inches(centimeters):
    """
    Convert centimeters to inches.
    
    Conversion formula: 1 inch = 2.54 cm
    
    Args:
        centimeters (float): The length in centimeters
        
    Returns:
        float: The length converted to inches
    """
    inches = centimeters / 2.54
    return inches


# Main program
if __name__ == "__main__":
    print("Centimeters to Inches Converter")
    print("=" * 40)
    
    # Get input from user
    try:
        cm = float(input("Enter length in centimeters: "))
        result = cm_to_inches(cm)
        print(f"\n{cm} cm = {result:.2f} inches")
    except ValueError:
        print("Please enter a valid number")
    
    # Test cases
    print("\n" + "=" * 40)
    print("Test Cases:")
    print("=" * 40)
    test_values = [10, 25, 50, 100, 2.54]
    
    for cm in test_values:
        inches = cm_to_inches(cm)
        print(f"{cm} cm = {inches:.2f} inches")
