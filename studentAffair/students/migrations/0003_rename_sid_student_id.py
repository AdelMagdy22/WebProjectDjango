# Generated by Django 4.2.1 on 2023-05-24 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_student_id_student_dob_student_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='sid',
            new_name='id',
        ),
    ]
