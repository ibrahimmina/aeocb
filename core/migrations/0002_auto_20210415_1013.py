# Generated by Django 3.1.7 on 2021-04-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(blank=True),
        ),
    ]
