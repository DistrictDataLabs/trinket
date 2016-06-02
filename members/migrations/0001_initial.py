# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 22:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markupfield.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email_hash', models.CharField(editable=False, max_length=32)),
                ('organization', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('location', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('biography', markupfield.fields.MarkupField(blank=True, default=None, help_text=b'Edit in Markdown', null=True, rendered_field=True)),
                ('twitter', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('biography_markup_type', models.CharField(choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')], default=b'markdown', editable=False, max_length=30)),
                ('linkedin', models.URLField(blank=True, default=None, null=True)),
                ('_biography_rendered', models.TextField(editable=False, null=True)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'member_profiles',
            },
        ),
    ]
