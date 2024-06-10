# Generated by Django 5.0.6 on 2024-06-06 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipients', '0002_alter_recipients_description_alter_recipients_email_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipients',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AddField(
            model_name='recipients',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Менеджер рассылок'),
        ),
    ]