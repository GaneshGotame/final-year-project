# Generated by Django 5.0.6 on 2024-08-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm1', '0002_section_num_class_in_week'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Semester',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='department',
            new_name='semester',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meetingtime',
            name='time',
            field=models.CharField(choices=[('7:15 - 8:55', '7:15 - 8:55'), ('8:55 - 10:35', '8:55 - 10:35'), ('10:35 - 11:25', '10:35 - 11:25'), ('11:25 - 1:05', '11:25 - 1:05'), ('1:05 - 1:55', '1:05 - 1:55')], default='11:30 - 12:30', max_length=50),
        ),
    ]
