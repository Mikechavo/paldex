# Generated by Django 4.2.8 on 2024-02-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paldex', '0008_auto_20240221_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]