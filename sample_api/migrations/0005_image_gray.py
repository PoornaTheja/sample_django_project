# Generated by Django 4.1.4 on 2022-12-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_api', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='gray',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
