# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cloudinary.models
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
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha del evento')),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=1000)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image')),
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
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image')),
                ('categoria', models.ForeignKey(to='noticias.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title (optional)', blank=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image')),
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
