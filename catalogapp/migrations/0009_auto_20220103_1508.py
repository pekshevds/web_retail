# Generated by Django 3.0.2 on 2022-01-03 12:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0008_auto_20220103_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='country',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='product',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='uid',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
