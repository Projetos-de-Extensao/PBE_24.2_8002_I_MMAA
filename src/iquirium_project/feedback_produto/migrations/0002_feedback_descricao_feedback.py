# Generated by Django 5.1.2 on 2024-11-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='descricao_feedback',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]