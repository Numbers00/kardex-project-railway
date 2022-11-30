# Generated by Django 4.1.2 on 2022-10-19 08:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kardex_app', '0006_rename_labelmarkers_kardex_label_markers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kardex',
            name='extra_field_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='extra_fields',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='label_markers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='label_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None),
        ),
    ]