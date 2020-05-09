from django.db import models

# Create your models here.
class Veiculo(models.Model):
	CHOICES = (
		('CARRO', 'Carro'),
		('MOTO', 'Moto'),
		)

	tipo = models.CharField(max_length=6, choices=CHOICES)
	nome = models.CharField(max_length=10)
	ativo = models.BooleanField(default=True)

	def __str__(self):
		return self.nome


class Estacionamento(models.Model):
	nome    = models.CharField(max_length=16)
	cap_max = models.IntegerField()

	def __str__(self):
		return self.nome

class Vaga(models.Model):
	nome    = models.CharField(max_length=16)
	ocupada = models.BooleanField(default=False)
	estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

class RegistroEstacionamento(models.Model):
	veiculo = models.ForeignKey(Veiculo, models.SET_NULL, blank=True,null=True,)
	vaga = models.ForeignKey(Vaga, models.SET_NULL, blank=True,null=True,)
	data_entrada = models.DateField(auto_now=True)
	data_saida = models.DateField(blank=True, null=True)
