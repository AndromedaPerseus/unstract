# Generated by Django 4.2.1 on 2024-06-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0002_connectorinstance_connector_metadata_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectorinstance',
            name='connector_mode',
            field=models.CharField(choices=[(0, 'UNKNOWN'), (1, 'FILE_SYSTEM'), (2, 'DATABASE'), (3, 'MANUAL_REVIEW')], db_comment='0: UNKNOWN, 1: FILE_SYSTEM, 2: DATABASE, 3: MANUAL_REVIEW', default=0),
        ),
    ]
