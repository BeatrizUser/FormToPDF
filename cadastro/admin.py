from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome_do_Cliente', 'Cidade', 'gerar_relatorio')
    fieldsets = (
        ('Informações Gerais', {
            'fields': ['Nome_do_Cliente']
        }),
        ('Endereço', {
            'fields': ['Endereco_faturamento', ('Cidade', 'CEP', 'Tipo_Empresa')],
        }),
    )