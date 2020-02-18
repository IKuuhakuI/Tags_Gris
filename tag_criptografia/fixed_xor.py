def fixed_xor(entrada_1, entrada_2):
	if len(entrada_1) != len(entrada_2):
		return -1

	hex_list_1 = list(entrada_1)
	hex_list_2 = list(entrada_2)

	tam_hex_num = len(hex_list_1)

	xor_list = [0] * tam_hex_num * 4

	for count in range(tam_hex_num):
		# converte a string hexa da primeira entrada em decimal
		try:
			this_byte_num_1 = list(bin(int(hex_list_1[count], 16)))
		except:
			this_byte_num_1 = list(bin(int(hex_list_1[count])))

		# converte a string hexa da segunda entrada em decimal
		try:
			this_byte_num_2 = list(bin(int(hex_list_2[count], 16)))
		except:
			this_byte_num_2 = list(bin(int(hex_list_2[count])))	

		this_byte_num_1.pop(0)
		this_byte_num_1.pop(0)
		this_byte_num_2.pop(0)
		this_byte_num_2.pop(0)
	
		for tamanho in range(4 - len(this_byte_num_1)):
			this_byte_num_1.insert(0, '0')

		for tamanho in range(4 - len(this_byte_num_2)):
			this_byte_num_2.insert(0, '0')

		print(this_byte_num_1)
		print(this_byte_num_2)

	return 0	

################################################

def main():
	entrada_1 = input()
	entrada_2 = input()

	fixed_xor(entrada_1, entrada_2)

main()
