# Generated by Django 4.0.4 on 2022-07-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
