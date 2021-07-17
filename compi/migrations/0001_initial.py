# Generated by Django 3.1.1 on 2021-07-14 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200, unique=True)),
                ('is_open', models.BooleanField(default=False)),
                ('image', models.ImageField(default='default.jpg', upload_to='comp_image')),
                ('submission_date', models.CharField(max_length=100)),
                ('result_date', models.CharField(max_length=100)),
                ('contender_limit', models.IntegerField()),
                ('constraint', models.CharField(choices=[('g', 'Passing Grade'), ('t', 'Top Rank')], default='Top Rank', max_length=15)),
                ('constraint_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smule_name', models.CharField(max_length=50, unique=True)),
                ('line_name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='contenders_images')),
                ('password', models.CharField(max_length=100)),
                ('included', models.BooleanField(default=False)),
                ('competition', models.ManyToManyField(to='compi.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('dq', 'Disqualified'), ('p', 'Passed'), ('f', 'Failed'), ('o', 'ongoing')], max_length=100)),
                ('status_comment', models.CharField(max_length=100)),
                ('contender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compi.contender')),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='judges_images')),
                ('competitions', models.ManyToManyField(to='compi.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compi.entry')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compi.judge')),
            ],
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compi.competition')),
            ],
        ),
    ]