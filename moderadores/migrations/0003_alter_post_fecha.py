# Generated by Django 5.0.1 on 2024-01-28 06:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderadores', '0002_rename_moderador_moderadore_alter_moderadore_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
