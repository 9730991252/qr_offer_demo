# Generated by Django 5.1.1 on 2024-09-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_remove_qr_code_id_alter_qr_code_tag_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_code',
            name='tag_number',
            field=models.UUIDField(default='e32', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
