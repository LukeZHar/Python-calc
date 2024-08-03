def binary_to_decimal(binary):
    decimal = 0
    binary_length = len(binary)
    
    for i in range(binary_length):
        # Get the current bit (from left to right)
        bit = int(binary[binary_length - 1 - i])  # reverse index for positional value
        # Convert to decimal (bit * 2^position)
        decimal += bit * (2 ** i)
    
    return decimal

# Example usage
if __name__ == "__main__":
    binary_input = "1010"  # Example binary input
    decimal_output = binary_to_decimal(binary_input)
    print(f"The decimal value of binary '{binary_input}' is {decimal_output}.")
