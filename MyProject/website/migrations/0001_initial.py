# Generated by Django 5.1.6 on 2025-02-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(max_length=10)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_phone', models.CharField(max_length=100)),
                ('emp_address', models.CharField(max_length=200)),
                ('emp_is_active', models.BooleanField(default=False)),
                ('emp_department', models.CharField(max_length=100)),
            ],
        ),
    ]
