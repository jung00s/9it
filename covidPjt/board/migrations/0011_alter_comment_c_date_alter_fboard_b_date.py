# Generated by Django 4.0.2 on 2022-03-08 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_alter_comment_c_date_alter_fboard_b_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='c_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 8, 17, 46, 46, 997655), null=True),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 8, 17, 46, 46, 997655)),
        ),
    ]
