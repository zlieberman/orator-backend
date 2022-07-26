# Generated by Django 4.0.6 on 2022-07-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='public',
            field=models.BooleanField(default=False, null=True),
        ),
         migrations.AlterField(
            model_name='Assignment',
            name='correctness_level',
            fields=models.CharField(choices=[('NONE', 'None'), ('CLOSE', 'Close'), ('EXACT', 'Exact')], default='EXACT', max_length=5, null=True),
        ),
    ]
