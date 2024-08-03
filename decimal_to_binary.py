def decimal_to_binary (decimal):
	# your code here
	if decimal == 0:
		return "0"

	binary = ""
	while decimal > 0:
		remainder = decimal % 2
		binary = str(remainder) + binary
		decimal = decimal // 2

	return binary
print(decimal_to_binary(10))
