# Generated by Django 3.0.7 on 2020-10-24 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asadeye_api', '0008_auto_20201024_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asadeye_api.Products'),
        ),
    ]
