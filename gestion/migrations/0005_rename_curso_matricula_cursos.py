# Generated by Django 4.2.7 on 2023-11-22 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_asignatura_remove_funcionario_jefatura_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='curso',
            new_name='cursos',
        ),
    ]
