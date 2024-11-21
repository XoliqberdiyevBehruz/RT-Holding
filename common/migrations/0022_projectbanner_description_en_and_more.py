# Generated by Django 4.2 on 2024-11-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_alter_contactphonenumber_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectbanner',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='projectbanner',
            name='description_ko',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='projectbanner',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='projectbanner',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='projectbanner',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projectbanner',
            name='title_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projectbanner',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projectbanner',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
