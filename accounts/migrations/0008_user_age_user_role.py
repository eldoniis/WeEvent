# Generated by Django 4.1.6 on 2023-10-13 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]