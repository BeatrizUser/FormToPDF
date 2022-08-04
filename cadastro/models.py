from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone




class Cliente(models.Model):
    CNPJCPF = (
        ('CNPJ', 'Pessoa Jurídica'),
        ('CPF', 'Pessoa Física'),
    )
    
    Nome_do_Cliente = models.CharField(max_length=100, verbose_name=('Nome'))
    Data_Aniversario = models.DateField(default='')
    Tipo_Pessoa = models.CharField(max_length=4, choices= CNPJCPF)
    CNPJ_CPF = models.CharField(max_length = 20)
    Cadastrado_em = models.DateTimeField(default=timezone.now)
    Regiao = models.CharField(max_length = 20)
    Inscricao_Estadual = models.CharField(max_length = 20)
    Inscricao_Municipal = models.CharField(max_length = 20)
    Contato = models.CharField(max_length = 20)
    Inscricao_Suframa = models.CharField(max_length = 20)
    Desconto = models.CharField(max_length = 20)
    Vendedor = models.CharField(max_length = 20)
    Endereco_faturamento = models.CharField(max_length = 20)
    Numero = models.CharField(max_length = 6)
    Complemento = models.CharField(max_length = 20)
    Prazo_pg = models.CharField(max_length = 20)
    Bairro = models.CharField(max_length = 20)
    Pais = models.CharField(max_length = 20, default='Brasil')
    UF = models.CharField(max_length = 20)
    Reter_iss = models.CharField(max_length = 20)
    Guia_pg = models.CharField(max_length = 20)
    Data_Atualiazacao = models.CharField(max_length = 20)
    Cidade = models.CharField(max_length = 20)
    Codigo = models.CharField(max_length = 20)
    CEP = models.CharField(max_length = 9)
    Ramo_Atividade = models.CharField(max_length = 20)
    Tipo_Empresa = models.CharField(max_length = 20)
    Desc_Nat_Juridica = models.CharField(max_length = 20)
    Nome_Fantasia = models.CharField(max_length = 20)
    Descricao_CNAE = models.CharField(max_length = 20)
    Situacao_cadastral = models.CharField(max_length = 20)
    Data_abertura = models.CharField(max_length = 20)
    Data_Pesquisa = models.CharField(max_length = 20)
    Observacoes = models.CharField(max_length = 20)
    Endereco_Entrega = models.CharField(max_length = 20)
    Endereco_Cobranca= models.CharField(max_length = 20)
    Telefones_emails = models.CharField(max_length = 20)

    class Meta:
        ordering = ['Nome_do_Cliente']

    def gerar_relatorio(self):
        return mark_safe("""<a href=\"/relatorio/%s/\" target="_blank"><img src=\"/static/images/relatorio.png\" alt="Gerar Relatorio"></a>""" % self.id)

    def __str__(self):
        return self.Nome_do_Cliente
