# Generated by Django 4.2.12 on 2024-05-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_rename_sample_ration_experiment_sample_ratio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='teams_count',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
