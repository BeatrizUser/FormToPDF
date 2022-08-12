# Generated by Django 4.0.4 on 2022-08-10 19:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0021_alter_cliente_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_responsavel', models.CharField(max_length=20)),
                ('cargo_responsavel', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to='cadastro.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fornecedor', models.CharField(max_length=100, verbose_name='Nome')),
                ('nome_fantasia', models.CharField(max_length=100, verbose_name='Nome Fantasia')),
                ('data_aniversario', models.DateField(default='')),
                ('responsavel', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('cnpj', models.CharField(max_length=20)),
                ('inscricao_estadual', models.CharField(max_length=20)),
                ('pix_1', models.CharField(max_length=20)),
                ('pix_2', models.CharField(max_length=20)),
                ('Observacoes', models.CharField(max_length=20)),
                ('Cadastrado_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('cad_emails', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='cadastro.emails')),
                ('endereco_fornecedor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco_fornecedor', to='cadastro.endereco')),
            ],
            options={
                'ordering': ['nome_fornecedor'],
            },
        ),
    ]
