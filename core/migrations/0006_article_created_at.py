# Generated by Django 3.1.6 on 2021-03-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_article_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]