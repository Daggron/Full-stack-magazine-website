# Generated by Django 2.0 on 2018-10-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
