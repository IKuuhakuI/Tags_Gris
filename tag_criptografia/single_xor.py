def single_byte_xor(entrada):
	dic = {}
	max_key = ["", 0]

	for count in range(len(entrada)):
		try:
			qtd = int(dic[entrada[count]]) + 1

		except:
			qtd = 1

		dic[entrada[count]] = qtd

		if(max_key[0] == ""):
			max_key[0] = entrada[count]
			max_key[1] = qtd

		elif(max_key[1] < qtd):
			max_key[0] = entrada[count]
			max_key[1] = qtd			

	print(dic)

	print(max_key)
	
	# e = 0x65
	letra_e = ['1', '0', '0', '0', '0', '0', '1'] 

single_byte_xor('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
