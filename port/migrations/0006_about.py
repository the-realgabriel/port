# Generated by Django 5.0.3 on 2024-10-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0005_delete_item_rename_body_body_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
    ]
