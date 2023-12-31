# Generated by Django 4.2.3 on 2023-08-29 11:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uang',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('red_freq', models.IntegerField()),
                ('green_freq', models.IntegerField()),
                ('blue_freq', models.IntegerField()),
                ('value', models.PositiveIntegerField()),
            ],
        ),
    ]
