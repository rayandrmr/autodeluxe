# Generated by Django 4.1.3 on 2023-03-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0006_alter_contactdb_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='productde',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('PRICE', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='checkoutdb',
            name='PHONE',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
