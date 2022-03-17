# Generated by Django 3.2.5 on 2022-03-01 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0023_mydocuments_mydocumentstype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mydocuments',
            name='filecourse',
        ),
        migrations.AddField(
            model_name='mydocuments',
            name='mydocumentstype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.mydocumentstype'),
        ),
    ]