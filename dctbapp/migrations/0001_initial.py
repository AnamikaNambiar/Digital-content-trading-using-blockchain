# Generated by Django 2.0.9 on 2023-12-01 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=200)),
                ('c_date', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('r_date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('usertype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('IMAGE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dctbapp.image')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=500)),
                ('contacts', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dctbapp.login')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dctbapp.user'),
        ),
        migrations.AddField(
            model_name='image',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dctbapp.user'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dctbapp.user'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dctbapp.user'),
        ),
    ]
