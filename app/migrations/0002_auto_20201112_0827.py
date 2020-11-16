# Generated by Django 3.1.2 on 2020-11-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.SmallIntegerField(choices=[(1, 'manual'), (2, 'automatic'), (3, 'robot')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(),
        ),
    ]