from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone


Sim_Nao = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )

class Fornecedor(models.Model):
    
    nome_fornecedor = models.CharField(max_length=100, verbose_name=('Nome'))
    nome_fantasia = models.CharField(max_length=100, verbose_name=('Nome Fantasia'))
    data_aniversario = models.DateField(default='')
    responsavel = models.CharField(max_length = 20)
    endereco_fornecedor = models.OneToOneField('Endereco', on_delete=models.CASCADE, related_name='endereco_fornecedor', blank=True, null=True)
    telefone = models.CharField(max_length = 20)
    fax = models.CharField(max_length = 20)
    cnpj = models.CharField(max_length = 20)
    inscricao_estadual = models.CharField(max_length = 20)

    pix_1 = models.CharField(max_length = 20)
    pix_2 = models.CharField(max_length = 20)
    
    Observacoes = models.CharField(max_length = 200)

    cad_emails = models.OneToOneField('Email', on_delete=models.CASCADE, related_name='emails', blank=True, null=True)

    Cadastrado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['nome_fornecedor']


    def __str__(self):
        return self.nome_fornecedor

class Email(models.Model):

    fornecedor_nome = models.ForeignKey('Fornecedor', on_delete=models.CASCADE, related_name = 'fornecedor', blank=True)
    nome_responsavel = models.CharField(max_length = 20)
    cargo_responsavel = models.CharField(max_length = 20)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email

class Endereco(models.Model):
    Endereco_choices = (
        ('Faturamento', 'Endereço de Faturamento'),
        ('Entrega', 'Endereço de Entrega'),
    )

    Tipo_de_Endereço = models.CharField(max_length = 20, choices=Endereco_choices)
    Logradouro = models.CharField(max_length = 20)
    Numero = models.CharField(max_length = 6)
    Complemento = models.CharField(max_length = 20)
    Bairro = models.CharField(max_length = 20)
    Pais = models.CharField(max_length = 20, default='Brasil')
    UF = models.CharField(max_length = 20)
    Cidade = models.CharField(max_length = 20)
    Codigo = models.CharField(max_length = 20)
    CEP = models.CharField(max_length = 9)
    Responsavel = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name = 'responsavel', blank=True)

    def __str__(self):
        return self.Logradouro

class Cliente(models.Model):
    CNPJCPF = (
        ('CNPJ', 'Pessoa Jurídica'),
        ('CPF', 'Pessoa Física'),
    )
    
    Nome_do_Cliente = models.CharField(max_length=100, verbose_name=('Nome'))
    Data_Aniversario = models.DateField(default='')
    Tipo_Pessoa = models.CharField(max_length=4, choices= CNPJCPF)
    CNPJ_CPF = models.CharField(max_length = 20)
    Regiao = models.CharField(max_length = 20)
    Inscricao_Estadual = models.CharField(max_length = 20)
    Inscricao_Municipal = models.CharField(max_length = 20)
    Contato = models.CharField(max_length = 20)
    Inscricao_Suframa = models.CharField(max_length = 20)
    Desconto = models.CharField(max_length = 20)
    Vendedor = models.CharField(max_length = 20)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='endereco', blank=True, null=True)
    Reter_iss = models.CharField(max_length = 20)
    Guia_pg = models.CharField(max_length = 20)
    Data_Atualiazacao = models.CharField(max_length = 20)
    Ramo_Atividade = models.CharField(max_length = 20)
    Tipo_Empresa = models.CharField(max_length = 20)
    Desc_Nat_Juridica = models.CharField(max_length = 20)
    Nome_Fantasia = models.CharField(max_length = 20)
    Descricao_CNAE = models.CharField(max_length = 20)
    Situacao_cadastral = models.CharField(max_length = 20)
    Data_abertura = models.CharField(max_length = 20)
    Data_Pesquisa = models.CharField(max_length = 20)
    Observacoes = models.CharField(max_length = 20)
    Telefones_emails = models.CharField(max_length = 20)
    Cadastrado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['Nome_do_Cliente']

    def gerar_relatorio(self):
        return mark_safe("""<a href=\"/relatorio/pdf/%s/\" target="_blank"><img src=\"/static/images/relatorio.png\" alt="Gerar Relatorio"></a>""" % self.id)

    def __str__(self):
        return self.Nome_do_Cliente

class Produto(models.Model):
    Nome_do_Produto = models.CharField(max_length=100)
    Csit_Tributaria = models.CharField(max_length=100)
    Patrimonio_NCM = models.CharField(max_length=100)
    Cest = models.CharField(max_length=100)
    Numero_Serie = models.CharField(max_length=100)
    Pedidos = models.CharField(max_length=100)
    Validade = models.CharField(max_length=100)
    Pendência = models.CharField(max_length=100)
    Preco_uni = models.CharField(max_length=100)
    Uni_medida = models.CharField(max_length=100)
    Data_Cadatro = models.CharField(max_length=100)
    Data_Atualizacao = models.CharField(max_length=100)
    Descricao = models.CharField(max_length=100)
    Numero_Certificado = models.CharField(max_length=100)
    Certificado = models.CharField(max_length=100, choices = Sim_Nao)

