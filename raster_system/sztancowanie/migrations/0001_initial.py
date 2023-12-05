# Generated by Django 4.2.6 on 2023-10-25 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sztancowanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('client', models.CharField(max_length=80)),
                ('wykrojnik', models.CharField(max_length=30)),
                ('szt_ordered', models.DecimalField(decimal_places=0, max_digits=10)),
                ('szt_done', models.DecimalField(decimal_places=0, max_digits=10)),
                ('szt_status', models.BooleanField(default=False)),
                ('szt_plan_date', models.DateField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]