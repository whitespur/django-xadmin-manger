# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-06-24 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    # operations = [
    #     migrations.CreateModel(
    #         name='Activity',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('Product_logic_id', models.CharField(blank=True, max_length=45, verbose_name='产品日志id')),
    #             ('title', models.CharField(blank=True, max_length=45, verbose_name='活动标题')),
    #             ('pic_src', models.CharField(blank=True, max_length=45, verbose_name='活动地址')),
    #             ('content', models.CharField(blank=True, max_length=45, verbose_name='活动内容')),
    #             ('create_time', models.CharField(blank=True, max_length=45, verbose_name='创建日期')),
    #             ('remark1', models.CharField(blank=True, max_length=45, verbose_name='')),
    #             ('remark2', models.CharField(blank=True, max_length=45, verbose_name='')),
    #             ('remark3', models.CharField(blank=True, max_length=45, verbose_name='')),
    #         ],
    #         options={
    #             'verbose_name': '活动',
    #             'verbose_name_plural': '活动',
    #             'db_table': 'activity',
    #         },
    #     ),
    #     migrations.CreateModel(
    #         name='Log',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('user_id', models.CharField(blank=True, max_length=45, verbose_name='用户id')),
    #             ('conversion_id', models.TextField(blank=True, verbose_name='对话id')),
    #             ('question', models.TextField(blank=True, verbose_name='问题')),
    #             ('answer', models.TextField(blank=True, verbose_name='答案')),
    #             ('create_time', models.DateTimeField(blank=True, verbose_name='创建日期')),
    #             ('intent', models.CharField(blank=True, max_length=255)),
    #         ],
    #         options={
    #             'verbose_name': '日志信息',
    #             'verbose_name_plural': '日志信息',
    #             'db_table': 'qa_log',
    #         },
    #     ),
    #     migrations.CreateModel(
    #         name='Product',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('pid', models.CharField(blank=True, max_length=45)),
    #             ('cat_lv1', models.CharField(blank=True, max_length=45)),
    #             ('cat_lv2', models.CharField(blank=True, max_length=45)),
    #             ('cat_lv3', models.CharField(blank=True, max_length=45)),
    #             ('series', models.CharField(blank=True, max_length=45, verbose_name='系列')),
    #             ('product', models.CharField(blank=True, max_length=45, verbose_name='产品名称')),
    #             ('product_en', models.CharField(blank=True, max_length=512, verbose_name='产品英文名')),
    #             ('intro', models.CharField(blank=True, max_length=512, verbose_name='产品介绍')),
    #             ('capacity', models.CharField(blank=True, max_length=512, verbose_name='容量')),
    #             ('price', models.CharField(blank=True, max_length=45, verbose_name='价格')),
    #             ('color', models.CharField(blank=True, max_length=45, verbose_name='颜色')),
    #             ('color_series', models.CharField(blank=True, max_length=45, verbose_name='颜色系列')),
    #             ('is_best_color', models.IntegerField(blank=True)),
    #             ('color_image', models.CharField(blank=True, max_length=45)),
    #             ('color_series_image', models.CharField(blank=True, max_length=45)),
    #             ('is_new', models.IntegerField(blank=True)),
    #             ('is_best', models.IntegerField(blank=True)),
    #             ('efficacy', models.CharField(blank=True, max_length=512)),
    #             ('efficacy_words', models.CharField(blank=True, max_length=512)),
    #             ('skin_type', models.CharField(blank=True, max_length=512)),
    #             ('complexion', models.CharField(blank=True, max_length=512)),
    #             ('image_name', models.CharField(blank=True, max_length=255)),
    #             ('image', models.CharField(blank=True, max_length=512)),
    #             ('link', models.CharField(blank=True, max_length=512)),
    #             ('mini_app_link', models.CharField(blank=True, max_length=512)),
    #             ('series_link', models.CharField(blank=True, max_length=512)),
    #             ('use_steps', models.CharField(blank=True, max_length=512)),
    #             ('cat_link', models.CharField(blank=True, max_length=512)),
    #             ('create_time', models.DateTimeField(blank=True, verbose_name='创建日期')),
    #             ('update_time', models.DateTimeField(blank=True, verbose_name='更新日期')),
    #             ('activity', models.CharField(blank=True, max_length=16)),
    #             ('ec_image_name', models.CharField(blank=True, max_length=255)),
    #             ('ec_image_link', models.CharField(blank=True, max_length=255)),
    #             ('ec_use_steps', models.CharField(blank=True, max_length=512)),
    #             ('ec_link', models.CharField(blank=True, max_length=512)),
    #             ('ec_activity', models.CharField(blank=True, max_length=16)),
    #         ],
    #         options={
    #             'verbose_name': '产品信息',
    #             'verbose_name_plural': '产品信息',
    #             'db_table': 'product',
    #         },
    #     ),
    #     migrations.CreateModel(
    #         name='QaLogEc',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('user_id', models.CharField(blank=True, max_length=255, verbose_name='用户id')),
    #             ('session_id', models.TextField(blank=True, verbose_name='session_id')),
    #             ('source_type', models.CharField(blank=True, max_length=16, verbose_name='来源类型')),
    #             ('question', models.TextField(blank=True, verbose_name='问题')),
    #             ('answer', models.TextField(blank=True, verbose_name='答案')),
    #             ('create_time', models.DateTimeField(blank=True, verbose_name='创建时间')),
    #             ('intent', models.CharField(blank=True, max_length=255, verbose_name='intent')),
    #         ],
    #         options={
    #             'verbose_name': '日志EC',
    #             'verbose_name_plural': '日志EC',
    #             'db_table': 'qa_log_ec',
    #         },
    #     ),
    #     migrations.CreateModel(
    #         name='WxLog',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('openid', models.CharField(max_length=11)),
    #             ('question', models.TextField()),
    #             ('answer', models.TextField()),
    #             ('create_time', models.DateTimeField()),
    #         ],
    #         options={
    #             'verbose_name': '微信日志信息',
    #             'verbose_name_plural': '微信日志信息',
    #             'db_table': 'wx_qa_log',
    #         },
    #     ),
    # ]
