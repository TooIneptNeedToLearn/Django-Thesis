# Generated by Django 5.0.2 on 2024-03-04 08:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_thesis_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thesis',
            options={'ordering': ['-published_date']},
        ),
        migrations.AlterField(
            model_name='thesis',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddIndex(
            model_name='thesis',
            index=models.Index(fields=['-published_date'], name='content_the_publish_597cfd_idx'),
        ),
    ]