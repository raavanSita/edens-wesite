# Generated by Django 3.1.5 on 2021-01-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newArrivals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('discription', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('img_url', models.CharField(max_length=3000)),
            ],
        ),
    ]
