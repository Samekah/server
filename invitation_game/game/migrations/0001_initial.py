# Generated by Django 3.2.7 on 2021-09-03 14:57

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hair_id', models.IntegerField()),
                ('skin_id', models.IntegerField()),
                ('dress_id', models.IntegerField()),
                ('eyes_id', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'characters',
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'invitations',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=100)),
                ('incorret_answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=3)),
            ],
            options={
                'verbose_name_plural': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'scores',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.character')),
                ('host_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('invitation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.invitation')),
                ('questions', models.ManyToManyField(blank=True, to='game.Question')),
                ('scores', models.ManyToManyField(blank=True, to='game.Score')),
            ],
            options={
                'verbose_name_plural': 'games',
            },
        ),
    ]