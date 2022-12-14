# Generated by Django 4.0.4 on 2022-08-04 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_cliente_delete_relatorio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Inscricao_estadual',
            new_name='Inscricao_Estadual',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='Inscricao_municipal',
            new_name='Inscricao_Municipal',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='CNPJ_CPF',
            field=models.CharField(choices=[('CNPJ', 'Pessoa Jurídica'), ('CPF', 'Pessoa Física')], max_length=4),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Cadastrado_em',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
