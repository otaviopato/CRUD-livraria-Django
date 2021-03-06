# Generated by Django 4.0.5 on 2022-06-12 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_alter_livro_atualizado_em_alter_livro_criado_em'),
        ('autores', '0002_alter_autor_options_alter_autorlivro_options_and_more'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='autorlivro',
            index_together=set(),
        ),
        migrations.AlterField(
            model_name='autor',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 16, 13, 23, 39341), help_text='Data de criação do registro', verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='autorlivro',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 16, 13, 23, 40075), help_text='Data de criação do registro', verbose_name='Criado em'),
        ),
        migrations.AlterUniqueTogether(
            name='autorlivro',
            unique_together={('autor_id', 'livro_id')},
        ),
    ]
