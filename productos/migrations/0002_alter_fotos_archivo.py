# Generated by Django 5.1 on 2024-10-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='archivo',
            field=models.ImageField(upload_to='fotos/'),
        ),
    ]
