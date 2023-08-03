# Generated by Django 4.0.4 on 2022-05-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('email', models.CharField(max_length=111)),
                ('subject', models.CharField(max_length=111)),
                ('message', models.TextField(max_length=11111)),
            ],
            options={
                'verbose_name_plural': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Labours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('phone_no', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('total_project_done', models.IntegerField()),
                ('Audio_visual', models.BooleanField(default=False)),
                ('Electrical', models.BooleanField(default=False)),
                ('Maintenance', models.BooleanField(default=False)),
                ('Plumbing', models.BooleanField(default=False)),
                ('Tiling', models.BooleanField(default=False)),
                ('Wiring', models.BooleanField(default=False)),
                ('arival_price', models.IntegerField()),
                ('desc', models.TextField()),
                ('total_certificate', models.IntegerField()),
                ('certificate_1_name', models.CharField(blank=True, max_length=500)),
                ('certificate_1_img', models.ImageField(blank=True, upload_to='pics')),
                ('certificate_2_name', models.CharField(blank=True, max_length=500)),
                ('certificate_2_img', models.ImageField(blank=True, upload_to='pics')),
                ('certificate_3_name', models.CharField(blank=True, max_length=500)),
                ('certificate_3_img', models.ImageField(blank=True, upload_to='pics')),
                ('certificate_4_name', models.CharField(blank=True, max_length=500)),
                ('certificate_4_img', models.ImageField(blank=True, upload_to='pics')),
                ('Facebook_link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Labours',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('message', models.TextField(max_length=11111)),
                ('labour', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('zip', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('test', models.CharField(max_length=111)),
            ],
        ),
    ]