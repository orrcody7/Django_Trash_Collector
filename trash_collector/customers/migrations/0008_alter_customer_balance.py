# Generated by Django 3.2.6 on 2021-09-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_alter_customer_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
