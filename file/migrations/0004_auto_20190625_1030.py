# Generated by Django 2.2 on 2019-06-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20190625_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='number_id',
            field=models.IntegerField(default='8711', unique=True),
        ),
        migrations.AlterField(
            model_name='fir_details',
            name='fir_number',
            field=models.IntegerField(default='1187'),
        ),
        migrations.AlterField(
            model_name='register',
            name='reg_id',
            field=models.IntegerField(default='6556'),
        ),
    ]
