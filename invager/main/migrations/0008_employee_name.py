# Generated by Django 3.2.7 on 2021-09-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210903_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='A', max_length=100),
            preserve_default=False,
        ),
    ]
