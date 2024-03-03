# Generated by Django 5.0.2 on 2024-03-03 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='blog',
        ),
        migrations.AddField(
            model_name='blogs',
            name='blog_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.category'),
        ),
    ]
