# Generated by Django 3.1.3 on 2020-12-09 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0008_comment_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]
