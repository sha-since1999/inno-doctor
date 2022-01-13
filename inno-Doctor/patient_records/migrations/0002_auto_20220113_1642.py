# Generated by Django 2.2.24 on 2022-01-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalpatientsummary',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=None, max_length=10),
        ),
    ]