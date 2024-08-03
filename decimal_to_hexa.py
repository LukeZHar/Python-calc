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
    decimal_input = 255  # Example decimal input
    hex_output = decimal_to_hexadecimal(decimal_input)
    print(f"The hexadecimal value of decimal '{decimal_input}' is {hex_output}.")
