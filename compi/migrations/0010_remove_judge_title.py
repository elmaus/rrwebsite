# Generated by Django 3.1.1 on 2021-07-16 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compi', '0009_judge_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judge',
            name='title',
        ),
    ]
