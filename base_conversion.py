def convert_to_decimal(number, base_from):
    """Convert a number from a given base to decimal."""
    decimal_value = 0
    number = number.upper()  # Handle lowercase letters in hex
    length = len(number)

    for i in range(length):
        digit = number[length - 1 - i]  # From least significant to most significant
        if '0' <= digit <= '9':
            decimal_value += int(digit) * (base_from ** i)
        elif 'A' <= digit <= 'F':
            decimal_value += (ord(digit) - ord('A') + 10) * (base_from ** i)
    
    return decimal_value

def convert_from_decimal(decimal_number, base_to):
    """Convert a decimal number to a given base."""
    if decimal_number == 0:
        return '0'
    
    result = ''
    while decimal_number > 0:
        remainder = decimal_number % base_to
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder - 10 + ord('A')) + result  # Convert to hex character
        decimal_number //= base_to
    
    return result

def base_conversion(number, base_from, base_to):
    """Convert a number from one base to another."""
    # First convert from the original base to decimal
    decimal_value = convert_to_decimal(number, base_from)
    # Then convert from decimal to the target base
    return convert_from_decimal(decimal_value, base_to)

# Example usage
if __name__ == "__main__":
    number_input = "1010"  # Example input number
    base_from = 2          # Base of the input number
    base_to = 16           # Target base for conversion

    converted_number = base_conversion(number_input, base_from, base_to)
    print(f"The number '{number_input}' from base {base_from} is '{converted_number}' in base {base_to}.")