# Generated by Django 3.1 on 2020-08-26 09:49

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('django_practical', '0004_auto_20200826_1015'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserOverride',
        ),
        migrations.CreateModel(
            name='UserOverride',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'UserOverrides',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
