# Generated by Django 4.0.4 on 2022-08-09 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0016_remove_cliente_cadastrar_endereço_cliente_endereco'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endereco',
            options={'ordering': ['Tipo_de_Endereço', 'Logradouro']},
        ),
    ]
