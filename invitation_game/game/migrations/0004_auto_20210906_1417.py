# Generated by Django 3.2.7 on 2021-09-06 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20210906_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='invitation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.invitation'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='side1',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='side1', to='game.game'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='side2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='side2', to='game.game'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wedding_url',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]