# Generated by Django 4.1.4 on 2022-12-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
