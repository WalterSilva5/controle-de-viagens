create table Viagem(
	motorista varchar(100) not null,
	auxiliar1 varchar(100),
	auxiliar2 varchar(100),
	cidade varchar(100),
	veiculo varchar(100),
	horariodesaida varchar(10),
	horariodechegada varchar(10),
	data date,
	observacoes varchar(250),
	idviagem integer primary key autoincrement
	); 
