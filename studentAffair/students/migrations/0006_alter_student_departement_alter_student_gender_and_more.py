# Generated by Django 4.2.1 on 2023-05-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_departement_alter_student_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='departement',
            field=models.CharField(choices=[('none', 'none'), ('CS', 'CS'), ('AI', 'AI'), ('IS', 'IS'), ('IT', 'IT'), ('DS', 'DS')], default='none', max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('inActive', 'inActive')], max_length=8),
        ),
    ]
