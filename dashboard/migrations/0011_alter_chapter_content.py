# Generated by Django 4.2.5 on 2024-04-03 11:47

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_chapter_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
