# Generated by Django 4.1.7 on 2023-03-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_rename_text_places_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='place_id',
            field=models.CharField(max_length=25),
        ),
    ]