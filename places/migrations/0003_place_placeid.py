# Generated by Django 3.2.14 on 2022-07-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='placeId',
            field=models.CharField(default='something', max_length=50, verbose_name='ID места'),
            preserve_default=False,
        ),
    ]
