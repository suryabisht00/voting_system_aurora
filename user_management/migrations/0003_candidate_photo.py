# Generated by Django 5.1.1 on 2024-10-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_citizendata_constituency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='photo',
            field=models.ImageField(default='Unknown', upload_to='photos/candidate_photos/'),
        ),
    ]
