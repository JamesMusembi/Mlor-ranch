# Generated by Django 4.1.7 on 2023-03-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_animalsranch_charateristics'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalsranch',
            name='Statistics',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
