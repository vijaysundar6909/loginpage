# Generated by Django 4.0.3 on 2022-03-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
