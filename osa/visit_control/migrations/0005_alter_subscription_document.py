# Generated by Django 4.2 on 2024-06-10 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visit_control', '0004_parent_chat_id_alter_group_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='visit_control.document', verbose_name='Документ'),
        ),
    ]
