# Generated by Django 4.0.5 on 2022-07-08 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebHome', '0004_sitios'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitios',
            name='proveedor_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebHome.proveedor'),
        ),
    ]