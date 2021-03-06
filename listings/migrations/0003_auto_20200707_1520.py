# Generated by Django 2.2.3 on 2020-07-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190921_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='bathrooms',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='bedrooms',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='garage',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='listings',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='square_metre',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='state',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='listings',
            name='zipcode',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
