hex_num = input()

hex_num = int(hex_num, 16)

hex_str = list(hex(hex_num))

hex_str.pop(0)
hex_str.pop(0)

bin_list = [0] * len(hex_str)

for idx in range(len(hex_str)):
	this_hex = int(hex_str[idx], 16)

	print(bin(this_hex))

	this_bin = list(bin(this_hex))
	this_bin.pop(0)
	this_bin.pop(0)

	tam_bin = 8 - len(this_bin)

	for count in range(tam_bin):
		this_bin.insert(0,'0')

	bin_list[idx] = this_bin

print(bin_list)
