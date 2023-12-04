# Generated by Django 4.2.7 on 2023-11-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Назва катергорії')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('activate', models.BooleanField(default=False, verbose_name='Active')),
            ],
        ),
    ]
