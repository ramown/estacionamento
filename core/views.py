from django.shortcuts import render, HttpResponse
from core.models import Estacionamento, RegistroEstacionamento, Vaga, Veiculo


# Create your views here.
def index(request):
	return HttpResponse('[OK]')

def monitor_page(request):
	dados = {'titulo': 'Monitor'}
	if request.POST:
		nome_veiculo = request.POST['busca_veiculo']
		try:
			veiculo = Veiculo.objects.get(nome=nome_veiculo)
			if veiculo:
				dados['veiculo'] = veiculo
				try:
					vaga = Vaga.objects.get(veiculo=veiculo)
					dados['vaga'] = vaga
				except Exception as e:
					dados['vaga'] = '--'
		except Exception:
			dados['vazio'] = 'Veículo não encontrado'
	return render(request, 'Monitor.html', dados)

