# Generated by Django 4.2.11 on 2024-03-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Fitness', 'Fitness'), ('Mental Wellbeing', 'Mental Wellbeing'), ('Life Coaching', 'Life Coaching'), ('General', 'General')], default='General', max_length=50),
        ),
    ]