# Generated by Django 3.2 on 2021-05-01 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
        ('notes', '0003_note_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.profile'),
        ),
    ]
