def hexadecimal_to_decimal(hexadecimal):
    """Convert a hexadecimal number (as a string) to decimal."""
    decimal = 0
    hex_length = len(hexadecimal)

    for i in range(hex_length):
        digit = hexadecimal[hex_length - 1 - i].upper()  # Reverse index for positional value
        decimal += int(digit, 16) * (16 ** i)  # Base 16 conversion

    return decimal

def decimal_to_binary(decimal):
    """Convert a decimal number to binary (as a string)."""
    if decimal == 0:
        return "0"

    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return binary

def hexadecimal_to_binary(hexadecimal):
    """Convert a hexadecimal number (as a string) to binary."""
    decimal_value = hexadecimal_to_decimal(hexadecimal)  # Convert Hex to Decimal
    binary_string = decimal_to_binary(decimal_value)      # Convert Decimal to Binary
    return binary_string

# Example usage
if __name__ == "__main__":
    hex_input = "1A"  # Example hexadecimal input
    binary_output = hexadecimal_to_binary(hex_input)
    print(f"The binary value of hexadecimal '{hex_input}' is {binary_output}.")
