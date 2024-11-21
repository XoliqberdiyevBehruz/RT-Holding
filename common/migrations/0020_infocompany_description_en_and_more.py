# Generated by Django 4.2 on 2024-11-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0019_alter_infocompany_options_alter_ourinfo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infocompany',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infocompany',
            name='description_ko',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infocompany',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infocompany',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infocompany',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infocompany',
            name='title_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infocompany',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infocompany',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourinfo',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ourinfo',
            name='text_ko',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ourinfo',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ourinfo',
            name='text_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ourinfo',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourinfo',
            name='title_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourinfo',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourinfo',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
