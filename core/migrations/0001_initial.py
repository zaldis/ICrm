# Generated by Django 5.0.6 on 2024-06-26 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_rename_organisation_customer_organization_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(choices=[('SE', 'Software Engineering'), ('DO', 'DevOps'), ('BD', 'Big Data')], help_text='What specialization does the customer need', max_length=30)),
                ('grade', models.CharField(choices=[('T1', 'Junior'), ('T2', 'Middle'), ('T3', 'Senior')], help_text='What grade does the customer need', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('approved_developer', models.ForeignKey(help_text='Developers who was approved for this request by the customer', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='approved_request_processes', to='user.developer')),
                ('customer', models.ForeignKey(help_text='Customer who requested new developer', on_delete=django.db.models.deletion.CASCADE, related_name='request_processes', to='user.customer')),
                ('suggested_developers', models.ManyToManyField(help_text='Developers who were suggested for this request by the delivery manager', related_name='request_processes', to='user.developer')),
            ],
        ),
    ]
