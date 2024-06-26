# Generated by Django 5.0.6 on 2024-05-25 16:48

import tasks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=30)),
                ('deadline', models.DateField(validators=[tasks.models.validate_deadline_date])),
                ('priority', models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')])),
            ],
        ),
    ]
