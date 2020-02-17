convert_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\
		'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',\
		'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',\
		'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',\
		'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',\
		'8', '9', '+', '-']

hex_num = input()

hex_list = [0] * len(hex_num)

for idx in range(len(hex_num)):
	try:
		hex_alg = int(hex_num[idx],16)
		hex_alg.pop(0)
		hex_alg.pop(0)

	except:
		hex_alg = hex_num[idx]
	
	hex_list[idx] = hex_alg

tam_hex_num = len(hex_list)

bin_list = [0] * tam_hex_num * 8

for idx in range(tam_hex_num):
	byte_list = [0] * 8
	try:
		this_hex = int(hex_list[idx], 16)

	except:
		this_hex = int(hex_list[idx])

	this_bin = list(bin(this_hex))
	this_bin.pop(0)
	this_bin.pop(0)

	tam_bin = 8 - len(this_bin)

	for count in range(tam_bin):
		this_bin.insert(0,'0')

	byte_list[idx] = this_bin

	for count in range(8):
		bin_list[(idx * 8) +  count] = byte_list[idx][count]

qtd_bits = len(bin_list)

print(bin_list)

lista_64 = []

# Caso quantidade de bits correta
if qtd_bits % 6 == 0:
	grupos_bits = int(qtd_bits / 6)

	for count in range(grupos_bits):
		idx = count * 6
		num_list = bin_list[idx :idx + 6]

		print(num_list)

		num_string = "".join(str(x) for x in num_list)

		number = int(num_string, 2)

		lista_64.append(convert_list[number])		

# Caso sobre 4 bits
elif qtd_bits % 6 == 4:
	print('caso 2')

# Caso sobre 2 bits
else:
	print('caso 3')

result = "".join(str(x) for x in lista_64)

print(result)
