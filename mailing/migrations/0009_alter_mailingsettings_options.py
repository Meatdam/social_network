# Generated by Django 5.0.6 on 2024-06-09 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0008_mailingmessage_owner_mailingsettings_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsettings',
            options={'permissions': [('change_mailingsettings_settings_status', 'Can change mailingsettings settings status')], 'verbose_name': 'Настройка отправки', 'verbose_name_plural': 'Настройки отправки'},
        ),
    ]