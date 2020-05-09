from django.contrib import admin
from core.models import Estacionamento, RegistroEstacionamento, Vaga, Veiculo


class RegistroAdmin(admin.ModelAdmin):
	list_display = ('veiculo', 'vaga', 'data_entrada', 'data_saida')


# Register your models here.
admin.site.register(Estacionamento)
admin.site.register(RegistroEstacionamento, RegistroAdmin)
admin.site.register(Vaga)
admin.site.register(Veiculo)
