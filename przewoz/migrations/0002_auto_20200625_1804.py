# Generated by Django 3.0.7 on 2020-06-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('przewoz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transit',
            name='arrival',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transit',
            name='departure',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
