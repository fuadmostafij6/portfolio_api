# Generated by Django 4.0 on 2021-12-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg', models.ImageField(blank=True, null=True, upload_to='asset/banner/bg/')),
                ('avater', models.ImageField(blank=True, null=True, upload_to='asset/banner/avater/')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
                ('image9', models.ImageField(blank=True, null=True, upload_to='asset/banner/barand/')),
            ],
        ),
    ]
