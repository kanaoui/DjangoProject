# Generated by Django 5.0.4 on 2024-04-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campagne', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campagne',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]