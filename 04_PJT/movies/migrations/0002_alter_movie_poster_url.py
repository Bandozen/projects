# Generated by Django 3.2.7 on 2023-03-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_url',
            field=models.CharField(max_length=300),
        ),
    ]
