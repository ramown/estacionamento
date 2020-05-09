Criação de um sistema para gerenciar o estacionamento

[] veiculo
	- nome
	- na_unidade

[] estacionamento
	- nome
	- capacidade máx
	* criar_vagas -> 

[] vaga
	- nome = nome['estacionamento']+numero
	- estacionamento [FK]
	- ocupada = False

[] transação
	OTO veiculo - OTO vaga - entrada - saida
	estrar_na_vaga(vaga)
		seleciona veiculo
	sair_da_vaga(veiculo)
		remover veiculo



#veiculo entra na unidade
	na_unidade = true

veiculo transitando no estacionamento

veiculo estacionar

veiculo transitando no estacionamento

veiculo passa o portão

veiculo sai da unidade
