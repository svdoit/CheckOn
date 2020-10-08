# Generated by Django 3.1.2 on 2020-10-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=200)),
                ('itemImg', models.ImageField(blank=True, upload_to='images/')),
                ('itemPrice', models.CharField(max_length=20)),
                ('category', models.IntegerField(max_length=10)),
            ],
        ),
    ]