# Generated by Django 3.0.2 on 2022-01-03 12:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0006_auto_20220103_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='uid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
    ]