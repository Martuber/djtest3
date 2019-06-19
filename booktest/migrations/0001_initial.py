# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('publish_date', models.DateTimeField(null=True)),
                ('reading_volume', models.IntegerField(null=True)),
                ('publisher', models.CharField(max_length=10, null=True)),
                ('comments', models.CharField(max_length=1000, null=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'BookInfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hero_name', models.CharField(max_length=10)),
                ('hero_age', models.IntegerField()),
                ('hero_comments', models.CharField(max_length=1000, null=True)),
                ('hero_like', models.CharField(max_length=200, null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('hero_book', models.ForeignKey(to='booktest.BookInfo')),
            ],
            options={
                'db_table': 'HeroInfo',
            },
        ),
    ]
