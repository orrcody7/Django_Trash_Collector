# Generated by Django 3.2.6 on 2021-08-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20210827_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(blank=True, default=None, max_length=50),
        ),
    ]