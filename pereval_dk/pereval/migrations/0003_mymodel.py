# Generated by Django 4.1.3 on 2023-09-18 20:55

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0002_images_image_1_images_image_2_images_image_3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
