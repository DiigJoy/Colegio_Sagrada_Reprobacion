# Generated by Django 4.2.7 on 2023-11-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_alter_funcionario_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='correo',
            field=models.EmailField(max_length=100),
        ),
    ]
