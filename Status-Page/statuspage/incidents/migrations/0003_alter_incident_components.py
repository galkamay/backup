# Generated by Django 4.1.2 on 2022-10-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_alter_component_options'),
        ('incidents', '0002_alter_incidentupdate_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='components',
            field=models.ManyToManyField(blank=True, null=True, related_name='incidents', to='components.component'),
        ),
    ]
