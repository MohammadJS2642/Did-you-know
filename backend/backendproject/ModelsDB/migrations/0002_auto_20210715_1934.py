# Generated by Django 3.2.5 on 2021-07-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsDB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='didyouknow',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='didyouknow',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]