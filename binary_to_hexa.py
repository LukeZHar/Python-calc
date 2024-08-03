def binary_to_decimal(binary):
    decimal = 0
    binary_length = len(binary)

    for i in range(binary_length):
        bit = int(binary[binary_length - 1 - i])  # Reverse index for positional value
        decimal += bit * (2 ** i)

    return decimal

def binary_to_hexadecimal(binary):
    decimal_value = binary_to_decimal(binary)  # Convert Binary to Decimal
    hex_string = decimal_to_hexadecimal(decimal_value)  # Convert Decimal to Hex
    return hex_string

def decimal_to_hexadecimal(decimal):
    if decimal == 0:
        return "0"
    
    hex_string = ""
    hex_digits = "0123456789ABCDEF"  # Hexadecimal digits

    while decimal > 0:
        remainder = decimal % 16
        hex_string = hex_digits[remainder] + hex_string
        decimal = decimal // 16
    
    return hex_string

# Example usage
if __name__ == "__main__":
    binary_input = "1010"  # Example binary input
    hex_output = binary_to_hexadecimal(binary_input)
    print(f"The hexadecimal value of binary '{binary_input}' is {hex_output}.")
