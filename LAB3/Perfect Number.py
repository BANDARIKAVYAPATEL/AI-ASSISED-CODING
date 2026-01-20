import math


def is_perfect_number(num):
    """
    Check whether a given number is a perfect number.
    
    A perfect number is a positive integer that is equal to the sum of its 
    proper positive divisors (divisors excluding the number itself).
    
    Examples:
        6 = 1 + 2 + 3 (divisors of 6)
        28 = 1 + 2 + 4 + 7 + 14 (divisors of 28)
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is perfect, False otherwise
    """
    # Perfect numbers must be positive
    if num <= 0:
        return False
    
    # 1 is not a perfect number
    if num == 1:
        return False
    
    # Calculate the sum of proper divisors
    divisor_sum = 1  # 1 is always a divisor for num > 1
    
    # Check divisors up to sqrt(num) for efficiency
    sqrt_num = int(math.sqrt(num))
    
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            divisor_sum += i
            # Add the complementary divisor if it's different
            if i != num // i:
                divisor_sum += num // i
    
    return divisor_sum == num


def get_perfect_number_info(num):
    """
    Get detailed information about whether a number is perfect.
    
    Args:
        num (int): The number to check
        
    Returns:
        dict: Dictionary containing classification and divisors
    """
    if num <= 0:
        return {
            "number": num,
            "is_perfect": False,
            "message": "Perfect numbers must be positive",
            "divisors": []
        }
    
    # Find all proper divisors
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    
    divisor_sum = sum(divisors)
    is_perfect = divisor_sum == num
    
    return {
        "number": num,
        "is_perfect": is_perfect,
        "divisors": divisors,
        "sum_of_divisors": divisor_sum,
        "message": f"{num} is {'a Perfect Number' if is_perfect else 'NOT a Perfect Number'}"
    }


def find_perfect_numbers(limit):
    """
    Find all perfect numbers up to a given limit.
    
    Args:
        limit (int): The upper limit to search
        
    Returns:
        list: List of perfect numbers up to the limit
    """
    perfect_numbers = []
    for num in range(1, limit + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers


# Test cases and demonstrations
if __name__ == "__main__":
    print("=" * 80)
    print("PERFECT NUMBER CHECKER")
    print("=" * 80)
    
    # Test cases
    test_numbers = [1, 5, 6, 10, 28, 100, 496, 500, 8128]
    
    print("\nDetailed Information for Test Numbers:\n")
    print(f"{'Number':<10} {'Status':<30} {'Divisors':<50}")
    print("-" * 80)
    
    for num in test_numbers:
        info = get_perfect_number_info(num)
        divisors_str = str(info["divisors"])[:47]
        status = "PERFECT" if info["is_perfect"] else "NOT PERFECT"
        print(f"{num:<10} {status:<30} {divisors_str}")
    
    # Detailed examples
    print("\n" + "=" * 80)
    print("DETAILED EXAMPLES:")
    print("=" * 80 + "\n")
    
    examples = [6, 28, 496]
    for num in examples:
        info = get_perfect_number_info(num)
        print(f"Number: {num}")
        print(f"Divisors (excluding {num}): {info['divisors']}")
        print(f"Sum: {' + '.join(map(str, info['divisors']))} = {info['sum_of_divisors']}")
        print(f"Result: {info['message']}\n")
    
    # Find perfect numbers up to a limit
    print("=" * 80)
    print("Perfect Numbers up to 10,000:")
    print("=" * 80 + "\n")
    
    perfect_nums = find_perfect_numbers(10000)
    print(f"Perfect Numbers: {perfect_nums}")
    print(f"Total found: {len(perfect_nums)}\n")
    
    # Performance test
    print("=" * 80)
    print("Performance Test - Large Numbers:")
    print("=" * 80 + "\n")
    
    large_test = [100000, 8128, 1000000]
    for num in large_test:
        result = is_perfect_number(num)
        status = "PERFECT" if result else "NOT PERFECT"
        print(f"{num}: {status}")
