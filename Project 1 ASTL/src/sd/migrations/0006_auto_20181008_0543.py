# Generated by Django 2.2.dev20181004154227 on 2018-10-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd', '0005_uq_event_urgent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uq_event',
            name='evt_type',
            field=models.CharField(choices=[('EV', 'event'), ('DL', 'deadline'), ('GL', 'goal')], default='EV', max_length=2),
        ),
    ]
