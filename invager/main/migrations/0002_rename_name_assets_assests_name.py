# Generated by Django 3.2.7 on 2021-09-02 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='name',
            new_name='assests_name',
        ),
    ]
