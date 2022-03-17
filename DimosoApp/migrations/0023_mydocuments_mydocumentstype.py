# Generated by Django 3.2.5 on 2022-03-01 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0022_chatmessages'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDocumentsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('year', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('owner', models.CharField(blank=True, max_length=200, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('year', models.CharField(blank=True, max_length=200, null=True)),
                ('filecourse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.filecourse')),
            ],
        ),
    ]
