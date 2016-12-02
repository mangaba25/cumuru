# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-02 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOndeComer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Categoria_OndeComer',
            },
        ),
        migrations.CreateModel(
            name='ImageOndecomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images-capa', verbose_name='Imagem')),
                ('decription', models.CharField(blank=True, max_length=100, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Imagem_Ondecomer',
            },
        ),
        migrations.CreateModel(
            name='OndeComer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(blank=True, max_length=100, verbose_name='Identificador')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='cumuruxatiba/images-ondecomer', verbose_name='Imagem_1')),
                ('decription_1', models.CharField(blank=True, max_length=100, verbose_name='Descrição-1')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='cumuruxatiba/images-ondecomer', verbose_name='Imagem_2')),
                ('decription_2', models.CharField(blank=True, max_length=100, verbose_name='Descrição-2')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='cumuruxatiba/images-ondecomer', verbose_name='Imagem_3')),
                ('decription_3', models.CharField(blank=True, max_length=100, verbose_name='Descrição-3')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='cumuruxatiba/images-ondecomer', verbose_name='Imagem_4')),
                ('decription_4', models.CharField(blank=True, max_length=100, verbose_name='Descrição-4')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='E-mail')),
                ('contact', models.CharField(blank=True, max_length=100, verbose_name='Contato')),
                ('site', models.CharField(blank=True, max_length=100, verbose_name='Site')),
                ('link', models.CharField(blank=True, max_length=120, verbose_name='link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ondecomer.CategoryOndeComer', verbose_name='Category_OndeComer')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'OndeComer',
            },
        ),
    ]