# Generated by Django 3.1.6 on 2021-03-31 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210331_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='article_image')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='core.article')),
            ],
        ),
    ]
