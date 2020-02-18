def fixed_xor(entrada_1, entrada_2):
	if len(entrada_1) != len(entrada_2):
		return -1

	hex_list_1 = list(entrada_1)
	hex_list_2 = list(entrada_2)

	tam_hex_num = len(hex_list_1)

	bin_list_1 = [0] * tam_hex_num * 4
	bin_list_2 = [0] * tam_hex_num * 4

	for count in range(tam_hex_num):
		# converte a string hexa da primeira entrada em decimal
		try:
			this_hex_num_1 = int(hex_list_1[count], 16)
		except:
			this_hex_num_1 = int(hex_list_1[count])

		# converte a string hexa da segunda entrada em decimal
		try:
			this_hex_num_2 = int(hex_list_2[count], 16)
		except:
			this_hex_num_2 = int(hex_list_2[count])	

		print(this_hex_num_1)
		print(this_hex_num_2)

	return 0	

################################################

def main():
	entrada_1 = input()
	entrada_2 = input()

	fixed_xor(entrada_1, entrada_2)

main()
