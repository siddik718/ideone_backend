# Generated by Django 4.2 on 2023-05-02 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('url', models.CharField(default=uuid.uuid4, editable=False, max_length=100)),
            ],
        ),
    ]
