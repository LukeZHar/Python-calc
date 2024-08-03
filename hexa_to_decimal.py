def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    hex_length = len(hexadecimal)

    for i in range(hex_length):
        digit = hexadecimal[hex_length - 1 - i].upper()  # Reverse index for positional value
        decimal += int(digit, 16) * (16 ** i)  # Base 16 conversion

    return decimal

# Example usage
if __name__ == "__main__":
    hex_input = "FF"  # Example hexadecimal input
    decimal_output = hexadecimal_to_decimal(hex_input)
    print(f"The decimal value of hexadecimal '{hex_input}' is {decimal_output}.")