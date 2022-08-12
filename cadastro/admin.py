from django.contrib import admin
from django import forms
from .models import Cliente, Produto, Endereco, Email, Fornecedor

class ClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['CNPJ_CPF'].widget.attrs['class'] = 'mask-cpf'

        self.fields['endereco'].queryset = Endereco.objects.filter(
            Responsavel = self.instance.id,
        )

    class Meta:
        model = Cliente
        fields = '__all__'

    class Media:
        js = (
            "jquery.mask.min.js",
            "custom.js",
        )
class FornecedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FornecedorForm, self).__init__(*args, **kwargs)

        self.fields['cad_emails'].queryset = Email.objects.filter(
            fornecedor_nome = self.instance.id,
        )

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    form = ClientForm
    list_display = ('Nome_do_Cliente', 'Tipo_Pessoa', 'gerar_relatorio')
    fieldsets = (
        ('Informações Gerais', {
            'fields': ['Nome_do_Cliente', 'Data_Aniversario', 'Tipo_Pessoa', 'CNPJ_CPF', 'Contato', 'endereco']
        }),
        ('Informações Pessoa Jurídica', {
            'fields': [('Nome_Fantasia', 'Tipo_Empresa'),('Ramo_Atividade', 'Descricao_CNAE'),('Situacao_cadastral', 'Inscricao_Estadual', 'Inscricao_Municipal'),('Desc_Nat_Juridica','Telefones_emails'),('Observacoes')],
        }),
    )

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('Nome_do_Produto',)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('Tipo_de_Endereço', 'Logradouro', 'Responsavel')

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    form = FornecedorForm
    list_display = ('nome_fornecedor',)