# Generated by Django 3.2.5 on 2022-07-15 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_feature_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='created_at',
        ),
        migrations.AddField(
            model_name='feature',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
