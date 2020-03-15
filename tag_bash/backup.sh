#!/bin/bash

echo "Informe o(s) path(s) do(s) arquivo(s)/diretorio(s) que deseja fazer backup"
echo "(Separe arquivos diferentes com um espaco):"
read backup_files

destino="./logs"

sleep 1

if [ ! -d $destino ];then
	echo "Criando pasta logs"
	mkdir logs
	
	sleep 1
fi

hora=$(date +%H-%M-%S)
dia=$(date +%Y-%m-%d)
hostname=$(hostname -s)

arquivo="$hostname-$dia-$hora.tar.gz"

echo "Verificando existencia de arquivos com mais de 3 dias no backup"

sleep 1

find $destino/* -mtime +2 -exec echo removendo arquivo {} \;
find $destino/* -mtime +2 -exec rm -rf {} \;

sleep 1

if test -f $destino/$arquivo; then
	sleep 1

	echo "Removendo copia existente"

	sleep 1

	rm -rf $destino/$arquivo

	sleep 1

	echo "Copia removida com sucesso"
fi

sleep 1

echo "Realizando backup: $backup_files para $destino/$arquivo"

sleep 1

tar -zcvf $destino/$arquivo $backup_files

sleep 1

echo "Backup realizado com sucesso"

ls -lh $destino
