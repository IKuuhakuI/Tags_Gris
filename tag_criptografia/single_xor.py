def single_xor(entrada, caractere, tamanho):
	xor_byte_list = []

	for count in range(tamanho):
		if entrada[count] != caractere[count]:
			xor_byte_list.append('1')
		
		else:
			xor_byte_list.append('0')
	
	return xor_byte_list	

##################################

def join_hex(frase):
	hex_list = []	

	for count in range(0, len(frase),2):
		resultado = hex_to_byte(frase[count], frase[count+1])
		
		hex_list.append(resultado)

	return hex_list

#############################################

def get_byte(entrada):
	try:
		byte = list(bin(int(entrada, 16)))
	except:
		byte = list(bin(int(entrada)))

	byte.pop(0)
	byte.pop(0)

	for count in range(8 - len(byte)):
		byte.insert(0,'0')

	return byte

###########################################

def byte_to_ascii(entrada):
	number = int("".join(str(x) for x in entrada), 2)
	caractere = str(chr(number))		

	return caractere

##########################################

def hex_to_byte(entrada_1, entrada_2):
	byte_1 = get_byte(entrada_1)
	byte_2 = get_byte(entrada_2)

	resultado = [0] * 8

	for count in range(4):
		byte_1.pop(0)
		byte_2.pop(0)

	for count in range(4):
		resultado[count] = byte_1[count]
		resultado[count + 4] = byte_2[count]

	resultado = "".join(str(x) for x in resultado)		

	return resultado

############################################

def decifrar(entrada, current_letter):
	dic = {}
	max_list = ["", 0]

	entrada_hex_list = join_hex(entrada)
	
	tam_entrada_hex_list = len(entrada_hex_list)
		
	for count in range(tam_entrada_hex_list):
		try:
			qtd = int(dic[entrada_hex_list[count]]) + 1

		except:
			qtd = 1

		dic[entrada_hex_list[count]] = qtd

		if(max_list[0] == ""):
			max_list[0] = entrada_hex_list[count]
			max_list[1] = qtd

		elif(max_list[1] < qtd):
			max_list[0] = entrada_hex_list[count]
			max_list[1] = qtd			

	max_key_byte = list(max_list[0])

	xor_byte_list = single_xor(max_key_byte, current_letter, 8)

	lista_resultado = []

	for count in range(tam_entrada_hex_list):
		this_xor_byte = single_xor(entrada_hex_list[count], xor_byte_list, 8)

		ascii_char = byte_to_ascii(this_xor_byte)

		lista_resultado.append(ascii_char)

	resultado = "".join(str(x) for x in lista_resultado)

	return resultado


##################################

def main():
	# Em ordem dos caracteres mais usados da lingua inglesa
	caracteres_mais_usados = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'h',\
			      'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g',\
			      'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

	resultado = "Não achei um resultado satisfatório"

	for idx in range(len(caracteres_mais_usados)):
		print("Caractere atual:", caracteres_mais_usados[idx])
		print()

		caractere = get_byte(ord(caracteres_mais_usados[idx]))
		teste = decifrar('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', caractere)

		print("Resultado testado:", teste)
		print()
		

		is_ok = input("Caso resultado satisfatório, digite ok: ")

		if is_ok == "ok":
			resultado = teste
			print()
			break

		print()
		print("#######################################\n")

	print("Resultado final:", resultado)
main()
