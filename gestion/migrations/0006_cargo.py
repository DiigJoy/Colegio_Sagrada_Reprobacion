# Generated by Django 4.2.5 on 2023-11-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_rename_curso_matricula_cursos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.TextField(max_length=100)),
            ],
        ),
    ]
