# Generated by Django 3.2.5 on 2021-08-12 07:26

import app1.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
                ('author_language', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_a', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('12', 'aparna'), ('13', 'manu'), ('14', 'ganesh'), ('15', 'ajay'), ('16', 'anusha')], max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('present', models.BooleanField(null=True)),
                ('num', models.IntegerField(null=True)),
                ('phnum', models.BigIntegerField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('student_updated', models.DateTimeField(auto_now=True, null=True)),
                ('student_date', models.DateTimeField(default=datetime.datetime(2021, 8, 12, 7, 26, 38, 732091, tzinfo=utc))),
                ('rating', models.TextField(blank=True, help_text='plz fill rating starting from 5 star ', null=True)),
                ('email', models.EmailField(default='mi@gmail.com', max_length=254)),
                ('Profile_pic', models.ImageField(null=True, upload_to='images/%y/%m/%d')),
                ('Resume', models.FileField(null=True, upload_to='userfiles/%y/%m/%d')),
                ('comment', models.TextField(null=True, validators=[app1.models.comment])),
            ],
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.BigIntegerField()),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.employee')),
            ],
        ),
        migrations.CreateModel(
            name='novel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('novel_name', models.CharField(max_length=200)),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.author')),
            ],
        ),
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=200)),
                ('member', models.ManyToManyField(to='app1.Member')),
            ],
        ),
    ]