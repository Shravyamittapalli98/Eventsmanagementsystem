# Generated by Django 3.1.4 on 2021-10-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(max_length=20)),
                ('Event_cost', models.IntegerField()),
                ('Capacity', models.IntegerField()),
                ('Facilities', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'eventmngapp_events1',
            },
        ),
    ]
