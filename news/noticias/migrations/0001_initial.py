# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(verbose_name=b'Fecha del evento')),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha de Publicacion')),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=1000)),
                ('categoria', models.ForeignKey(to='noticias.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('matricula', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
