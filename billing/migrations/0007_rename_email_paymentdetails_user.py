# Generated by Django 4.2 on 2023-08-18 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_rename_user_paymentdetails_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='email',
            new_name='user',
        ),
    ]
