# Generated by Django 5.1.7 on 2025-05-29 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animeApp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programpoints',
            options={'ordering': ('-pk',), 'verbose_name': 'За счет чего достигается программа', 'verbose_name_plural': 'За счет чего достигается программа'},
        ),
    ]
