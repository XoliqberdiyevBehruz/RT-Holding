# Generated by Django 4.2 on 2024-11-20 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_customerfeedback_user_feedback_en_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productmedia',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='productmedia',
            name='order',
        ),
    ]