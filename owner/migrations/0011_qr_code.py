# Generated by Django 5.1.1 on 2024-09-16 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0010_delete_qr_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qr_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_number', models.IntegerField(unique=True)),
                ('scan_status', models.IntegerField(default=0)),
                ('redeem_status', models.IntegerField(default=0)),
                ('generate_date', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('sr_num', models.IntegerField(null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
            ],
        ),
    ]
