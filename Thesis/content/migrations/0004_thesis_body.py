# Generated by Django 5.0.2 on 2024-03-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_thesis_department_thesis_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
