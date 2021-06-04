# Generated by Django 2.2.4 on 2019-10-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_knownfaces_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamousFaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=50)),
                ('real_name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('movies', models.CharField(max_length=1000)),
                ('awards', models.CharField(max_length=500)),
                ('external_links', models.CharField(max_length=5000)),
            ],
        ),
        migrations.AlterField(
            model_name='knownfaces',
            name='dob',
            field=models.CharField(max_length=30),
        ),
    ]
