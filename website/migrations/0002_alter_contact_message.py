# Generated by Django 4.2.3 on 2023-09-14 07:49

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
