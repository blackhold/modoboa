# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 13:20
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='pattern',
            field=models.CharField(db_index=True, max_length=253, unique=True, verbose_name='pattern'),
        ),
    ]
