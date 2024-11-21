# Generated by Django 4.2 on 2024-11-18 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_banner_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='service',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='common.service'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProjectCategory',
        ),
    ]