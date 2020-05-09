from django.shortcuts import render, HttpResponse, redirect
from core.models import Estacionamento, RegistroEstacionamento, Vaga, Veiculo


# Create your views here.
def index(request):
	return render(request, 'model-page.html')

def monitor_page(request):
	dados = {'titulo': 'Monitor'}
	if request.POST:
		nome_veiculo = request.POST['busca_veiculo']
		try:
			veiculo = Veiculo.objects.get(nome=nome_veiculo)
			if veiculo:
				dados['veiculo'] = veiculo

		except Exception:
			dados['vazio'] = 'Veículo não encontrado'
		try:
			vaga = Vaga.objects.get(veiculo=veiculo)
			dados['vaga'] = vaga
		except Exception as e:
			dados['vaga'] = '--'

	try:
		estacionamentos = Estacionamento.objects.all()
		dados['estacionamentos'] = estacionamentos
	except Exception as e:
		dados['no-estacionamento'] = 'Ainda sem estacionamento(s) cadastrado(s)'

	return render(request, 'monitor.html', dados)

def index_estacionamento(request, id):
	dados = {'id': id}
	try:
		estacionamento = Estacionamento.objects.get(id=id)
		dados['estacionamento'] = estacionamento
		try:
			vagas = Vaga.objects.filter(estacionamento=estacionamento)
			dados['vagas'] = enumerate(vagas)
		except Exception as e:
			raise e
	except Exception as e:
		raise e
	return render(request, 'estacionamento/index.html', dados)	

def new_estacionamento(request):
	if request.POST:
		nome = request.POST['nome']
		capacidade = request.POST['capacidade']
		try:
		 	ativo = True if request.POST['ativo'] is not None else False
		except Exception as e:
		 	ativo = False

		Estacionamento.objects.create(
			nome=nome,
			cap_max=capacidade,
			ativo = ativo
			)
		estacionamento = Estacionamento.objects.get(nome=nome)
		gerar_vagas(estacionamento)
		return redirect('/')
		
	return render(request, 'estacionamento/form.html')

def gerar_vagas(estacionamento):
	capacidade = estacionamento.cap_max
	for item in range(capacidade):
		nome = "V{} - {}".format(gerar_nome(item+1), estacionamento.nome)
		Vaga.objects.create(
			nome=nome,
			estacionamento=estacionamento
			)

def gerar_nome(numero):
	if(numero>0 and numero <10):
		return "00{}".format(numero)
	elif(numero>9 and numero <100):
		return "0{}".format(numero)
	else:
		return "{}".format(numero)
