# Generated by Django 4.1.7 on 2023-06-09 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='presenca',
            name='nome_professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor'),
        ),
    ]