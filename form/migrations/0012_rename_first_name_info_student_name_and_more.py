# Generated by Django 4.0.5 on 2022-06-20 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0011_alter_info_aadhar_number_alter_info_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='First_Name',
            new_name='Student_Name',
        ),
        migrations.RemoveField(
            model_name='info',
            name='Last_Name',
        ),
    ]