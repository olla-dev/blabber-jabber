# Generated by Django 4.1.3 on 2022-11-24 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_time_utc', models.DateTimeField()),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('SENT', 'Sent'), ('READ', 'Read'), ('DELETED', 'Deleted')], default='SENT', max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chatroom')),
            ],
            options={
                'ordering': ['-sent_time_utc'],
            },
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['sent_time_utc', 'id'], name='sent_time_utc_idx'),
        ),
        migrations.AddIndex(
            model_name='chatroom',
            index=models.Index(fields=['name', 'id'], name='name_idx'),
        ),
    ]
