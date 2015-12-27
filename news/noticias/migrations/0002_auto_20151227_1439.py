# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha del evento'),
        ),
    ]
