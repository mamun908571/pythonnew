# Generated by Django 4.2.7 on 2024-01-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_about_v_c_about_v_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Password',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
