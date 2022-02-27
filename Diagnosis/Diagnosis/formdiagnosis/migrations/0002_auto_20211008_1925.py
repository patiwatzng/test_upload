# Generated by Django 3.2.8 on 2021-10-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formdiagnosis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allergysymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coldsymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='musclesymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]