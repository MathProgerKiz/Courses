# Generated by Django 4.2.14 on 2024-07-24 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Courses', '0004_alter_coursesmodel_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificatesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Дата и время, когда был выдан сертификат')),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='Courses.coursesmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
