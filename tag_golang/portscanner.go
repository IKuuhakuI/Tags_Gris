package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("Teste")

	qtd_ports := 65535

	for i := 1; i < qtd_ports; i++ {
		fmt.Println(strconv.FormatInt(int64(i), 10))
	}
}
