# Generated by Django 2.1.5 on 2019-02-28 00:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])),
                ('mass', models.PositiveIntegerField()),
                ('distance', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Type must be greater than 1 character')])),
            ],
        ),
        migrations.AddField(
            model_name='star',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stars.Type'),
        ),
    ]
