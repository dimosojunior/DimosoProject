# Generated by Django 3.2.5 on 2022-03-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0025_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]