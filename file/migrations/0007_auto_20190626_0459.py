# Generated by Django 2.2.1 on 2019-06-26 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_auto_20190626_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='number_id',
            field=models.IntegerField(default='8792', unique=True),
        ),
        migrations.AlterField(
            model_name='fir_details',
            name='fir_number',
            field=models.IntegerField(default='7711'),
        ),
        migrations.AlterField(
            model_name='register',
            name='reg_id',
            field=models.IntegerField(default='2392'),
        ),
    ]
