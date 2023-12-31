# Generated by Django 4.1.7 on 2023-07-16 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_owner_alter_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.user'),
        ),
    ]
