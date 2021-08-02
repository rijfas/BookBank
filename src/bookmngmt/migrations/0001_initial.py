# Generated by Django 3.2.5 on 2021-08-02 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donate_book', models.CharField(blank=True, max_length=50, null=True)),
                ('donate_count', models.IntegerField(blank=True, default='1', null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.CharField(blank=True, choices=[('UG 1', 'UG 1'), ('UG 2', 'UG 2'), ('UG 3', 'UG 3'), ('PG 1', 'PG 1'), ('PG 2', 'PG 2')], max_length=20, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('donate_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, choices=[('UG 1', 'UG 1'), ('UG 2', 'UG 2'), ('UG 3', 'UG 3'), ('UG 4', 'UG 4'), ('UG 5', 'UG 5'), ('UG 6', 'UG 6'), ('PG 1', 'PG 1'), ('PG 2', 'PG 2'), ('PG 3', 'PG 3'), ('PG 4', 'PG 4')], max_length=20, null=True)),
                ('book_name', models.CharField(blank=True, max_length=50, null=True)),
                ('book_count', models.IntegerField(blank=True, default='0', null=True)),
                ('book_cover', models.ImageField(default='book_cover.jpg', upload_to='')),
                ('index_page', models.ImageField(default='index_page.jpg', upload_to='')),
                ('add_count', models.IntegerField(blank=True, default='0', null=True)),
                ('add_by', models.CharField(blank=True, max_length=50, null=True)),
                ('order_count', models.IntegerField(blank=True, default='0', null=True)),
                ('order_by', models.CharField(blank=True, max_length=50, null=True)),
                ('order_to', models.CharField(blank=True, max_length=50, null=True)),
                ('student_details', models.TextField()),
                ('phone_number', models.CharField(max_length=50)),
                ('alert_level', models.IntegerField(blank=True, default='0', null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookmngmt.course')),
            ],
        ),
    ]
