# Generated by Django 3.2.5 on 2022-06-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220623_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=50)),
                ('feature_file', models.FileField(upload_to='static/features/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
