create database db_processo;
use db_processo;

CREATE TABLE candidatos(
	CPF_candidato VARCHAR(14) PRIMARY KEY NOT NULL,
	nome VARCHAR(30) NOT NULL,
	curso VARCHAR(40) NOT NULL,
	contato_1 VARCHAR(40) NOT NULL,
	contato_2 VARCHAR(40)	
);

CREATE TABLE palestrantes(
	CPF_palestrante VARCHAR(14) PRIMARY KEY NOT NULL,
	nome VARCHAR(30) NOT NULL,
	formacao VARCHAR(40) NOT NULL,
	instituicao VARCHAR(40),
	contato_1 VARCHAR(40) NOT NULL,
	contato_2 VARCHAR(40)
);

CREATE TABLE palestras(
	ID_palestra INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	assunto VARCHAR(40) NOT NULL,
	data DATE NOT NULL,
	CPF_palestrante VARCHAR(14) NOT NULL,
	CONSTRAINT FK_CPF_palestrante FOREIGN KEY (CPF_palestrante)
    	REFERENCES palestrantes(CPF_palestrante)
);

CREATE TABLE tags(
	ID_tag INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ID_palestra INT NOT NULL,
	data_entrega DATETIME,
	descricao varchar(255) NOT NULL,
	CONSTRAINT FK_ID_palestra FOREIGN KEY (ID_palestra)
    	REFERENCES palestras(ID_palestra)
);

CREATE TABLE boletim(
	ID_boletim INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	CPF_candidato VARCHAR(14) NOT NULL,
	ID_tag INT NOT NULL,
	nota INT NOT NULL,
	atraso CHAR(1),
	CONSTRAINT FK_ID_tag FOREIGN KEY (ID_tag)
    	REFERENCES tags(ID_tag),
	CONSTRAINT FK_CPF_candidato FOREIGN KEY (CPF_candidato)
    	REFERENCES candidatos(CPF_candidato)
);

CREATE TABLE ouvintes(
	ID_ouvinte INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nome varchar(30) NOT NULL,
	CPF_ouvinte VARCHAR(14) NOT NULL, 
	ID_palestra int,
	FOREIGN KEY(ID_palestra) REFERENCES palestras(ID_palestra)
);
