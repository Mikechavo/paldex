# Generated by Django 5.0.1 on 2024-02-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('image', models.CharField(max_length=200, verbose_name='Image')),
                ('type', models.CharField(max_length=200, verbose_name='Type')),
                ('skill', models.CharField(max_length=200, verbose_name='Skill')),
                ('work', models.CharField(max_length=200, verbose_name='Work')),
                ('drops', models.CharField(max_length=200, verbose_name='Drops')),
                ('price', models.BigIntegerField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]