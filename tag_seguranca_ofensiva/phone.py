def decode(mensagem):
	dic = {'2':'a','22':'b','222':'c','3':'d','33':'e','333':'f','4':'g','44':'h','444':'i',
	       '5':'j','55':'k','555':'l','6':'m','66':'n','666':'o','7':'p','77':'q','777':'r',
	       '7777':'s','8':'t','88':'u','888':'v','9':'w','99':'x','999':'y','9999':'z'}

	tam_mensagem = len(mensagem)

	decode_list = []

	idx = 0

	while idx < tam_mensagem:
		check = mensagem[idx]

		check_idx = idx

		temp = [mensagem[idx]]
		somar = 1

		if check == " " or check == ":" or check == "!" or check == "\n" or check == "," or check == ".":
			decode_list.append(check)
			idx += 1
		
		else:
			while True:
				if idx+somar == tam_mensagem:
					if check_idx != idx+somar-1:
						temp.append(check)
					break

				elif check == mensagem[idx+somar]:
					temp.append(check)
					somar += 1
				else:
					break

			cel_num = "".join(str(x) for x in temp)
		
			this_char = dic[cel_num]
		
			decode_list.append(this_char)
	
			idx += somar

	decode_mes = "".join(str(x) for x in decode_list)

	return(decode_mes)

var = input()

print()

print(decode(var))
