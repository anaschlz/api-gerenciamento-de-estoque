# Generated by Django 5.0.6 on 2024-05-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nickname', models.CharField(default='', max_length=100)),
                ('user_task', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
