# Generated by Django 3.1.1 on 2020-09-12 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('cover_image', models.ImageField(upload_to='')),
                ('rating', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.category')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='people.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]