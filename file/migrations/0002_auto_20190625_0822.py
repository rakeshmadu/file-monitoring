# Generated by Django 2.2 on 2019-06-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('eligible', models.CharField(max_length=250)),
                ('number_id', models.IntegerField(default='6345', unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='reg_id',
            field=models.IntegerField(default='8534'),
        ),
    ]
