# Generated by Django 2.2 on 2022-04-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
