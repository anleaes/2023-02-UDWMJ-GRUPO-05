# Generated by Django 4.1 on 2023-12-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banho', models.CharField(max_length=50)),
                ('tosa', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=50)),
                ('animal', models.CharField(max_length=100)),
                ('raca', models.CharField(max_length=50)),
            ],
        ),
    ]