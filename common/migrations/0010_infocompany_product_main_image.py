# Generated by Django 4.2 on 2024-11-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_projectbanner_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='common/info-company/images/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('project_count', models.PositiveBigIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default='1', upload_to='common/product/main-image/'),
            preserve_default=False,
        ),
    ]
