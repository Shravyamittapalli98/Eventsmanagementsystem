# Generated by Django 3.1.4 on 2021-10-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmngapp', '0003_auto_20211021_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=20)),
                ('Query', models.TextField()),
            ],
        ),
    ]