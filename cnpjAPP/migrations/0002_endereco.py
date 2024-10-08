# Generated by Django 5.1 on 2024-08-25 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnpjAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(blank=True, max_length=200, null=True)),
                ('numero', models.CharField(blank=True, max_length=200, null=True)),
                ('cep', models.CharField(blank=True, max_length=200, null=True)),
                ('cnpj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cnpjAPP.empresa')),
            ],
        ),
    ]
