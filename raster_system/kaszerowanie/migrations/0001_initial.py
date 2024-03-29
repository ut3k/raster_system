# Generated by Django 4.2.6 on 2023-10-25 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kaszerowanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('print', models.CharField(max_length=80)),
                ('client', models.CharField(max_length=80)),
                ('material', models.CharField(default='mikrofala', max_length=80)),
                ('kasz_ordered', models.IntegerField(default=0)),
                ('kasz_done', models.IntegerField(default=0)),
                ('kasz_status', models.BooleanField(default=False)),
                ('kasz_plan_date', models.DateField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
