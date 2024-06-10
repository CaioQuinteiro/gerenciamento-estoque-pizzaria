# Generated by Django 5.0.6 on 2024-06-10 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=80)),
                ('qtde_estoque', models.IntegerField()),
                ('unidade_medida', models.CharField(max_length=5)),
            ],
        ),
    ]
