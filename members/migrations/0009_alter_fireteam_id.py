# Generated by Django 4.2.9 on 2024-02-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20240221_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fireteam',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
