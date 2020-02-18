def single_xor(entrada, caractere, tamanho):
	xor_byte_list = []

	for count in range(tamanho):
		if entrada[count] != caractere[count]:
			xor_byte_list.append('1')
		
		else:
			xor_byte_list.append('0')

	return xor_byte_list	

def decifrar(entrada):
	dic = {}
	max_list = ["", 0]

	for count in range(len(entrada)):
		try:
			qtd = int(dic[entrada[count]]) + 1

		except:
			qtd = 1

		dic[entrada[count]] = qtd

		if(max_list[0] == ""):
			max_list[0] = entrada[count]
			max_list[1] = qtd

		elif(max_list[1] < qtd):
			max_list[0] = entrada[count]
			max_list[1] = qtd			

	print(dic)
	print(max_list)
	
	try:
		max_key = list(bin(int(max_list[0], 16)))
	except:
		max_key = list(bin(int(max_list[0])))	

	max_key.pop(0)
	max_key.pop(0)

	for count in range(8 - len(max_key)):
		max_key.insert(0,'0')

	# e = 0x65
	letra_e = ['0', '1', '0', '0', '0', '0', '0', '1'] 
	
	xor_byte_list = single_xor(max_key, letra_e, 8)

	print(xor_byte_list)
decifrar('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
