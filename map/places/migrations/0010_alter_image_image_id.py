# Generated by Django 4.1.7 on 2023-03-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_image_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.IntegerField(db_index=True, default=1, unique=True),
        ),
    ]