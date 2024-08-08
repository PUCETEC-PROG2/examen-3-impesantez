# Generated by Django 4.2 on 2024-08-07 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('release_year', models.DateField()),
                ('genre', models.CharField(choices=[('Gótico', 'Gótico'), ('Metal', 'Metal'), ('Indie', 'Indie'), ('Rock', 'Rock')], max_length=30)),
                ('picture', models.ImageField(upload_to='album_image')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album_manager.artist')),
            ],
        ),
    ]
