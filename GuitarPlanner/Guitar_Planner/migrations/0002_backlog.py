# Generated by Django 3.2 on 2021-04-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guitar_Planner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
