# Generated by Django 2.2.10 on 2020-03-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='param1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='choice',
            name='param2',
            field=models.FloatField(default=0.0),
        ),
    ]
