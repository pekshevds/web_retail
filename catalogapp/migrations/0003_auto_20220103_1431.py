# Generated by Django 3.0.2 on 2022-01-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0002_auto_20220103_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='uid',
            field=models.UUIDField(blank=True, editable=False, null=True),
        ),
    ]