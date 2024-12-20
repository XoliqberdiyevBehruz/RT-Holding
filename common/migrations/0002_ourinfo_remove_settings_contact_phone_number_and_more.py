# Generated by Django 4.2 on 2024-11-18 10:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='settings',
            name='contact_phone_number',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='contact_phone_number2',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ContactPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Telefon raqami xalqaro formatda bo'lishi kerak: masalan, '+998901234567'.", regex='^\\+?[1-9]\\d{1,14}$')])),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_phone_numbers', to='common.settings')),
            ],
            options={
                'verbose_name': 'Contact Phone Number',
                'verbose_name_plural': 'Contact Phone Number',
            },
        ),
    ]
