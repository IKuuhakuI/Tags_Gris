package main

import (
	"fmt"
	"strconv"
	"net"
)

func main() {
	fmt.Println("Teste")

	qtd_ports := 65535

	for i := 1; i < qtd_ports; i++ {
		porta_atual := strconv.FormatInt(int64(i), 10)
		conn, erro := net.Dial("tcp", "127.0.0.1:" + porta_atual)

		if erro == nil {
			fmt.Println("Porta", i, "aberta")
			conn.Close()
		}
	}
}
