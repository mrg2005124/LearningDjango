# Generated by Django 4.2.10 on 2024-02-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_author_alter_category_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='ادرس'),
        ),
    ]