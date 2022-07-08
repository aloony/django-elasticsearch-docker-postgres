# Generated by Django 4.0.5 on 2022-07-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('imdb_title_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=1024)),
            ],
        ),
    ]