# Generated by Django 4.0 on 2022-04-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookweb', '0003_contact_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='availability',
            field=models.CharField(default='Lend', max_length=100),
        ),
    ]
