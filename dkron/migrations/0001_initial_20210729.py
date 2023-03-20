# Generated by Django 3.1.5 on 2021-07-29 08:53

from django.db import migrations, models


def data_fix(apps, schema_editor):
    apps.get_model("notifications", "Event").objects.update_or_create(name='dkron_failed_job')


class Migration(migrations.Migration):
    initial = True

    replaces = [
        ('dkron', '0001_initial_20210326'),
        ('dkron', '0004_remove_job_retries'),
        ('dkron', '0001_initial_v2'),
        ('dkron', '0001_initial'),
        ('dkron', '0002_auto_20190103_1758'),
        ('dkron', '0003_auto_20190110_1550'),
        ('dkron', '0004_auto_20190110_1804'),
        ('dkron', '0005_auto_20190213_1700'),
        ('dkron', '0006_job_retries'),
        ('dkron', '0001_squashed_0006_job_retries'),
        ('dkron', '0003_create_notify_event'),
        ('dkron', '0005_auto_20201104_0945'),
        ('dkron', '0002_job_notify_on_error'),
    ]

    dependencies = [
        ('notifications', '0001_initial_20210326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                (
                    'schedule',
                    models.CharField(
                        help_text='https://dkron.io/usage/cron-spec/ or "@parent JOBNAME" for dependent jobs',
                        max_length=255,
                    ),
                ),
                ('command', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('use_shell', models.BooleanField(default=False, help_text='/bin/sh -c "..."')),
                ('last_run_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('last_run_success', models.BooleanField(editable=False, null=True)),
                ('notify_on_error', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('can_use_dashboard', 'Can use the dashboard'),),
            },
        ),
        migrations.RunPython(data_fix),
    ]
