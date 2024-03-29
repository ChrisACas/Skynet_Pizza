# Generated by Django 2.2.4 on 2020-11-11 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crust', models.CharField(max_length=80)),
                ('sauce', models.CharField(max_length=80)),
                ('cheese', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_type', models.CharField(max_length=80)),
                ('ingredient', models.CharField(max_length=250)),
                ('nutritional', models.CharField(max_length=250)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generate.Pizza')),
            ],
        ),
    ]
