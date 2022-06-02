# Generated by Django 4.0.4 on 2022-06-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=300)),
                ('user_email', models.EmailField(default='', max_length=500)),
                ('user_phone', models.CharField(default='', max_length=50)),
                ('user_massage', models.TextField(default='')),
            ],
        ),
    ]