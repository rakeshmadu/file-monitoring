# Generated by Django 2.2 on 2019-06-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.IntegerField(default='8600')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('designation', models.CharField(choices=[('DGP', 'DGP'), ('ADGP', 'ADGP'), ('IGP/SIGP', 'IGP/SIGP'), ('DIGP', 'DIGP'), ('DSP', 'DSP'), ('SI', 'SI')], max_length=64)),
            ],
        ),
    ]
