# Generated by Django 5.0 on 2023-12-08 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raça', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('Aves', 'Aves'), ('Gato', 'Gato'), ('Cães', 'Cães')], max_length=255)),
                ('data_de_entrada', models.DateField()),
            ],
        ),
    ]
