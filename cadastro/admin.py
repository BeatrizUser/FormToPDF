from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome_do_Cliente', 'Cidade', 'gerar_relatorio')
    fieldsets = (
        ('Informações Gerais', {
            'fields': ['Nome_do_Cliente', 'Data_Aniversario', 'Tipo_Pessoa', 'CNPJ_CPF', 'Contato']
        }),
        ('Endereço', {
            'fields': [('Endereco_faturamento','Numero', 'Complemento'),('Bairro','Cidade','UF','CEP','Pais')],
        }),
        ('Informações Pessoa Jurídica', {
            'fields': [('Nome_Fantasia', 'Tipo_Empresa'),('Ramo_Atividade', 'Descricao_CNAE'),('Situacao_cadastral', 'Inscricao_Estadual', 'Inscricao_Municipal'),('Desc_Nat_Juridica','Telefones_emails'),('Observacoes')],
        }),
    )