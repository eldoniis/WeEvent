# Generated by Django 4.2.7 on 2023-11-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='esDestacado',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='esRecurrente',
        ),
        migrations.AddField(
            model_name='evento',
            name='puntuacion',
            field=models.FloatField(default=0),
        ),
    ]
