# Generated by Django 4.1.6 on 2023-10-25 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_alter_evento_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='categorias',
            field=models.CharField(choices=[('Deportivo', 'Deportivo'), ('Musical', 'Musical'), ('Gastronomico', 'Gastronomico'), ('Cultural', 'Cultural'), ('Ayuda Social', 'Ayuda Social'), ('Mascotas', 'Mascotas'), ('Academico', 'Academico'), ('Tecnologico', 'Tecnologico'), ('CompraVenta', 'CompraVenta')], default='', max_length=255),
        ),
    ]