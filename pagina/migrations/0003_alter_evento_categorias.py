# Generated by Django 4.1.6 on 2023-10-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_rename_fechalnicio_evento_fechainicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='categorias',
            field=models.CharField(choices=[], max_length=255),
        ),
    ]