# Generated by Django 4.0.4 on 2022-08-12 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0028_alter_fornecedor_observacoes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='fornecedor',
            new_name='fornecedor_nome',
        ),
    ]
