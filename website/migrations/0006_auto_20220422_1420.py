# Generated by Django 3.0.5 on 2022-04-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20220422_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.FloatField(blank=True, default='00.00', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='un3SQ8k0', max_length=8, null=True, unique=True),
        ),
    ]
