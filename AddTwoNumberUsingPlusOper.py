def multiply(a, b):
    # Handle negative numbers
    is_negative = (a < 0) ^ (b < 0)  # Result is negative if one of them is negative
    a, b = abs(a), abs(b)
    
    # Ensure minimal iterations by using the smaller number for iterations
    smaller, larger = (a, b) if a < b else (b, a)
    result = 0
    
    for _ in range(smaller):
        result += larger
    
    return -result if is_negative else result

# Example usage:
print(multiply(3, 5))  # Output: 15
print(multiply(-3, 5)) # Output: -15
print(multiply(3, -5)) # Output: -15
print(multiply(-3, -5))# Output: 15
