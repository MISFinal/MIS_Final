# Generated by Django 4.2.6 on 2023-12-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0002_inventory_userprofile_remove_sellerproduct_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='Default Category', max_length=255),
        ),
    ]