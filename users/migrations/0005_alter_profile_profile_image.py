# Generated by Django 3.2.9 on 2021-12-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user.png', null=True, upload_to='profiles/'),
        ),
    ]
