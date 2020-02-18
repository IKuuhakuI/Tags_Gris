def fixed_xor(entrada_1, entrada_2):
	if len(entrada_1) != len(entrada_2):
		return -1

	hex_list_1 = list(entrada_1)
	hex_list_2 = list(entrada_2)

	tam_hex_num = len(hex_list_1)

	xor_list = []

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

		for idx in range(4):
			if this_byte_num_1[idx] != this_byte_num_2[idx]:
				xor_list.append(1)

			else:
				xor_list.append(0)		
	
	lista_resultado = []

	for count in range(int(len(xor_list)/4)):
		idx = count * 4

		this_bit_str = "".join(str(x) for x in xor_list[idx:idx+4])

		bit_num = list(hex(int(this_bit_str, 2)))
		
		bit_num.pop(0)
		bit_num.pop(0)

		bit_num = "".join(str(x) for x in bit_num)		
	
		lista_resultado.append(bit_num)

	resultado = "".join(str(x) for x in lista_resultado)
			

	return resultado

################################################

def main():
	entrada_1 = input()
	entrada_2 = input()

	print(fixed_xor(entrada_1, entrada_2))

main()
