# Generated by Django 4.2.7 on 2024-01-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_companies'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='date_time',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]