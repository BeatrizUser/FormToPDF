# Generated by Django 4.0.4 on 2022-08-09 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0018_alter_endereco_options_alter_cliente_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='cadastro.endereco'),
        ),
    ]
