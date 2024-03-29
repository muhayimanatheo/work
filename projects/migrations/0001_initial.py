# Generated by Django 5.0 on 2024-01-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('products', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
            ],
        ),
    ]
