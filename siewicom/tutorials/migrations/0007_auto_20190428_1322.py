# Generated by Django 2.1.7 on 2019-04-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20190427_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': '文章表', 'verbose_name_plural': '文章表'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '分类表'},
        ),
        migrations.AlterModelOptions(
            name='tutorials',
            options={'verbose_name_plural': '课程表'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=20, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('html', 'HTML'), ('css', 'CSS'), ('os', 'OS')], max_length=20, verbose_name='分类名'),
        ),
        migrations.AlterField(
            model_name='tutorials',
            name='title',
            field=models.CharField(max_length=20, verbose_name='课程名称'),
        ),
    ]
