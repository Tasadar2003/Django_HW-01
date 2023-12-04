# Generated by Django 4.2.7 on 2023-11-18 22:48

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_category_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', djrichtextfield.models.RichTextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Kategoria', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
