# Generated by Django 4.2.1 on 2023-05-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer_users', '0002_dealerstatus_user_dealerstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_dealer',
            field=models.BooleanField(db_column='isdealer', default=False),
        ),
    ]