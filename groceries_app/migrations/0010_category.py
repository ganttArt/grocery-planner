# Generated by Django 3.1.2 on 2020-12-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries_app', '0009_auto_20201013_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
