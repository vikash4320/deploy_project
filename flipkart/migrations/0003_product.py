# Generated by Django 4.1 on 2023-09-05 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='upload/prodcut/')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipkart.category')),
            ],
        ),
    ]
