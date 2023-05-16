# Generated by Django 4.2.1 on 2023-05-10 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='main_pictures')),
                ('clienttitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title', to='admin1.clients')),
            ],
        ),
    ]