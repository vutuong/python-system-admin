# Generated by Django 3.2.5 on 2021-07-07 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ip_addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkaddress',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ip_addresses.networkaddress'),
        ),
    ]