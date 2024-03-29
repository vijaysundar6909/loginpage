# Generated by Django 4.0.3 on 2022-03-08 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('gmail', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('english', models.IntegerField()),
                ('tamil', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('science', models.IntegerField()),
                ('social', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('+1', 'class11'), ('+2', 'class12')], max_length=2)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('gmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mark.subject')),
            ],
        ),
    ]
