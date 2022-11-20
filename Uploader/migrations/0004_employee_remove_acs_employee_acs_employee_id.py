# Generated by Django 4.0.3 on 2022-06-13 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Uploader', '0003_alter_acs_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='acs',
            name='employee',
        ),
        migrations.AddField(
            model_name='acs',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Uploader.employee'),
        ),
    ]
