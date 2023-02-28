# Generated by Django 4.1.7 on 2023-02-28 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('image_id', models.IntegerField(null=True)),
                ('places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img', to='places.places')),
            ],
        ),
    ]