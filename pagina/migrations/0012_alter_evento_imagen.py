# Generated by Django 4.2.7 on 2023-11-20 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0011_alter_evento_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/'),
        ),
    ]
