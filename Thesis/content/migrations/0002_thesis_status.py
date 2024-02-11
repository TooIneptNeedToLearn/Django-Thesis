# Generated by Django 5.0.2 on 2024-02-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='status',
            field=models.CharField(choices=[('RJ', 'Rejected'), ('PB', 'Published'), ('UR', 'Under Review')], default='UR', max_length=2),
        ),
    ]
