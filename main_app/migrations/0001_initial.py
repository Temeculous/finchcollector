# Generated by Django 4.2.3 on 2023-07-06 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=40)),
                ('info', models.TextField(max_length=200)),
            ],
        ),
    ]