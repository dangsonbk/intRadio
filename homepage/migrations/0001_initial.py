# Generated by Django 2.1.5 on 2019-01-18 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50, verbose_name='Slug')),
                ('name', models.CharField(max_length=50, verbose_name='Tên category')),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_from', models.CharField(max_length=100, verbose_name='Tên người gửi')),
                ('l_to', models.CharField(max_length=100, verbose_name='Tên người nhận')),
                ('l_from_img', models.URLField(verbose_name='Ảnh người gửi')),
                ('l_to_img', models.URLField(max_length=250, verbose_name='Ảnh người nhận')),
                ('l_title', models.CharField(max_length=300, verbose_name='Title')),
                ('l_content', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Nội dung')),
                ('l_audio', models.URLField(max_length=250, verbose_name='Đường dẫn bài radio')),
                ('l_onair_date', models.DateField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Category')),
            ],
        ),
    ]
