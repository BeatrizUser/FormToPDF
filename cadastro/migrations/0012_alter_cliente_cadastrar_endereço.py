# Generated by Django 4.0.4 on 2022-08-09 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0011_alter_cliente_cadastrar_endereço'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Cadastrar_Endereço',
            field=models.ManyToManyField(help_text='Novo Endereço', max_length=200, to='cadastro.endereco'),
        ),
    ]
