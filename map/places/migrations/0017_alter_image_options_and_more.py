# Generated by Django 4.1.7 on 2023-03-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0016_rename_places_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_number']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_id',
            new_name='image_number',
        ),
    ]
