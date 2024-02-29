# Generated by Django 4.2.5 on 2024-02-28 20:20

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_course_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('chapter_number', models.IntegerField()),
                ('chapter_name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='chapter_name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='chapter_number',
        ),
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
        migrations.RemoveField(
            model_name='course',
            name='video',
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.course'),
        ),
    ]
