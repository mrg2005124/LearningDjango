# Generated by Django 4.2.10 on 2024-07-03 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article_is_special_alter_article_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='آدرس ایپی')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleHit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
                ('ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ipaddress')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='hit',
            field=models.ManyToManyField(blank=True, through='blog.ArticleHit', to='blog.ipaddress', verbose_name='بازدید'),
        ),
    ]