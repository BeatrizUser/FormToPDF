from django.db import models
from django.utils.safestring import mark_safe

class Cliente(models.Model):

    Nome_do_Cliente = models.CharField(max_length = 20, help_text = 'Nome_do_Cliente')
    Data_Aniversario = models.CharField(max_length = 20, help_text = 'Data_Aniversario')
    Tipo_Pessoa = models.CharField(max_length = 20, help_text = 'Física ou Juridica')
    CNPJ_CPF = models.CharField(max_length = 20, help_text = 'CNPJ_CPF')
    Cadastrado_em = models.CharField(max_length = 20, help_text = 'Cadastrado_em')
    Regiao = models.CharField(max_length = 20, help_text = 'Regiao')
    Inscricao_estadual = models.CharField(max_length = 20, help_text = 'Inscricao_estadual')
    Inscricao_municipal = models.CharField(max_length = 20, help_text = 'Inscricao_municipal')
    Contato = models.CharField(max_length = 20, help_text = 'Contato')
    Inscricao_Suframa = models.CharField(max_length = 20, help_text = 'Inscricao_Suframa')
    Desconto = models.CharField(max_length = 20, help_text = 'Desconto')
    Vendedor = models.CharField(max_length = 20, help_text = 'Vendedor')
    Endereco_faturamento = models.CharField(max_length = 20, help_text = 'Endereco_faturamento')
    Numero = models.CharField(max_length = 20, help_text = 'numero')
    Complemento = models.CharField(max_length = 20, help_text = 'Complemento')
    Prazo_pg = models.CharField(max_length = 20, help_text = 'Prazo_pg 1° 2° 3°')
    Bairro = models.CharField(max_length = 20, help_text = 'Bairro')
    Pais = models.CharField(max_length = 20, help_text = 'Pais')
    UF = models.CharField(max_length = 20, help_text = 'UF')
    Reter_iss = models.CharField(max_length = 20, help_text = 'Reter_iss')
    Guia_pg = models.CharField(max_length = 20, help_text = 'Guia_pg')
    Data_Atualiazacao = models.CharField(max_length = 20, help_text = 'Data_Atualiazacao')
    Cidade = models.CharField(max_length = 20, help_text = 'Cidade')
    Codigo = models.CharField(max_length = 20, help_text = 'Codigo')
    CEP = models.CharField(max_length = 20, help_text = 'CEP')
    Ramo_Atividade = models.CharField(max_length = 20, help_text = 'Ramo_Atividade')
    Tipo_Empresa = models.CharField(max_length = 20, help_text = 'Tipo_Empresa')
    Desc_Nat_Juridica = models.CharField(max_length = 20, help_text = 'Desc_Nat_Juridica')
    Nome_Fantasia = models.CharField(max_length = 20, help_text = 'Nome_Fantasia')
    Descricao_CNAE = models.CharField(max_length = 20, help_text = 'Descricao_CNAE')
    Situacao_cadastral = models.CharField(max_length = 20, help_text = 'Situacao_cadastral')
    Data_abertura = models.CharField(max_length = 20, help_text = 'Data_abertura')
    Data_Pesquisa = models.CharField(max_length = 20, help_text = 'Data_Pesquisa')
    Observacoes = models.CharField(max_length = 20, help_text = 'Observacoes')
    Endereco_Entrega = models.CharField(max_length = 20, help_text = 'Endereco_Entrega')
    Endereco_Cobranca= models.CharField(max_length = 20, help_text = 'Endereco_Cobranca')
    Telefones_emails = models.CharField(max_length = 20, help_text = 'Telefones_emails')

    class Meta:
        ordering = ['Nome_do_Cliente']

    def gerar_relatorio(self):
        return mark_safe("""<a href=\"/cadastro\" target="_blank"><img src=\"/static/images/relatorio.png\" alt="Gerar Relatorio"></a>""")

    def __str__(self):
        return self.Nome_do_Cliente
