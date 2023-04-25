# Generated by Django 4.2 on 2023-04-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=15)),
                ('author_name', models.CharField(max_length=200)),
                ('release_year', models.DateField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]