# Generated by Django 5.0.1 on 2024-02-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paldex', '0004_alter_palmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palmodel',
            name='image',
            field=models.URLField(verbose_name='Image'),
        ),
    ]
