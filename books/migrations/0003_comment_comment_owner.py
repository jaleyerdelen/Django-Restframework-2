# Generated by Django 4.1.5 on 2023-01-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_comment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_owner',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
