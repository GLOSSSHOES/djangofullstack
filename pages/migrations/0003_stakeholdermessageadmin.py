# Generated by Django 5.0.3 on 2024-03-26 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_stakeholdermessage_user_is_anonymous_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StakeholderMessageAdmin',
            fields=[
                ('stakeholdermessage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.stakeholdermessage')),
            ],
            bases=('pages.stakeholdermessage',),
        ),
    ]
