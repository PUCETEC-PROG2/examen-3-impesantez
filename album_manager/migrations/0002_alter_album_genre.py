# Generated by Django 4.2 on 2024-08-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Indie', 'Indie'), ('Rock', 'Rock'), ('Metal', 'Metal'), ('Gótico', 'Gótico')], max_length=30),
        ),
    ]
