# Generated by Django 5.0.1 on 2024-02-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paldex', '0003_alter_palmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palmodel',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
    ]
