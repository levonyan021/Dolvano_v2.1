# Generated by Django 4.1.5 on 2023-03-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_clock_info_header_1_clock_info_header_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clock',
            name='youtube_link',
            field=models.TextField(blank=True, null=True, verbose_name='Youtube Link'),
        ),
    ]
