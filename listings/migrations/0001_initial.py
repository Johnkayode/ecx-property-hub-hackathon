# Generated by Django 3.1.3 on 2020-12-02 17:00

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('description', models.TextField(max_length=500, verbose_name='description')),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('price', models.IntegerField(verbose_name='price')),
                ('is_new', models.BooleanField(default=False, verbose_name='is_new')),
                ('bedrooms', models.IntegerField(default=0, verbose_name='bedrooms')),
                ('bathrooms', models.IntegerField(default=0, verbose_name='bathrooms')),
                ('is_furnished', models.BooleanField(default=False, verbose_name='is furnished')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created_on')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='accounts.agent')),
                ('likes', models.ManyToManyField(related_name='listing_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=180, verbose_name='message')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='listings.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listings.listing')),
            ],
        ),
    ]