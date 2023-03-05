# Generated by Django 4.1.7 on 2023-03-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_places_description_short'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_id']},
        ),
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.IntegerField(db_index=True, default=1, null=True),
        ),
    ]