# Generated by Django 4.1 on 2023-12-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_setup', '0002_alter_menulink_new_tab_alter_menulink_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, verbose_name='title')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('show_header', models.BooleanField(default=True, verbose_name='show header?')),
                ('show_search', models.BooleanField(default=True, verbose_name='show search?')),
                ('show_menu', models.BooleanField(default=True, verbose_name='show menu?')),
                ('show_description', models.BooleanField(default=True, verbose_name='show description?')),
                ('show_pagination', models.BooleanField(default=True, verbose_name='show pagination?')),
                ('show_footer', models.BooleanField(default=True, verbose_name='show footer?')),
            ],
            options={
                'verbose_name': 'Setup',
                'verbose_name_plural': 'Setups',
            },
        ),
        migrations.AlterField(
            model_name='menulink',
            name='url_or_path',
            field=models.CharField(max_length=2048, verbose_name='Url or path'),
        ),
    ]
