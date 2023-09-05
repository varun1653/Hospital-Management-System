# Generated by Django 4.0.1 on 2022-04-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('AdministratorID', models.IntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=45)),
                ('password', models.CharField(default=None, max_length=45)),
                ('LastName', models.CharField(max_length=45)),
                ('EmailAddress', models.CharField(max_length=45)),
                ('PermantAddress', models.CharField(max_length=100)),
                ('Age', models.IntegerField(default=None)),
                ('Salary', models.IntegerField(default=None)),
                ('Shift', models.IntegerField(default=None)),
                ('BloodGroup', models.CharField(max_length=45)),
                ('contact', models.CharField(default=None, max_length=45)),
            ],
        ),
    ]