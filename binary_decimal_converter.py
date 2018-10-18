def decimal_to_binary(n): #Converts decimal to binary number
	binary = []
	while n > 0:
		binary.append(str(int(n%2)))
		if (n%2) == 1:
			n = n/2 - 0.5
		else:
			n = n/2
	binary.reverse()
	return "".join(binary)

def binary_to_decimal(n): #Converts decimal to binary number
	decimal = 0
	counter = 0
	for x in str(n)[::-1]:
		if int(x) == 1:
			decimal += (2**counter)
		counter += 1	
	return decimal

