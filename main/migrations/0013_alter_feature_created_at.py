# Generated by Django 3.2.5 on 2022-06-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_video_is_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='created_at',
            field=models.DateField(),
        ),
    ]
