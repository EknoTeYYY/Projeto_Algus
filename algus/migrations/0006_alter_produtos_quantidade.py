# Generated by Django 4.0.3 on 2022-04-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algus', '0005_alter_produtos_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='quantidade',
            field=models.IntegerField(),
        ),
    ]
