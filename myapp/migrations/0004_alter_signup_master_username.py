# Generated by Django 4.0.6 on 2022-08-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_master',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]