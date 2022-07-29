# Generated by Django 4.0.5 on 2022-07-08 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebHome', '0005_sitios_proveedor_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_enlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='sitios',
            name='bandwitch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sitios',
            name='tipo_enlace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebHome.tipo_enlace'),
        ),
    ]