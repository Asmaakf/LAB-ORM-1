# Generated by Django 5.0.3 on 2024-03-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Food', 'Food'), ('Tech', 'Tech')], default='General', max_length=64),
            preserve_default=False,
        ),
    ]
