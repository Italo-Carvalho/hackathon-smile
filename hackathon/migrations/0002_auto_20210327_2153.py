# Generated by Django 3.1.7 on 2021-03-28 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viagem',
            name='ativadade',
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='hospedagem',
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='restaurante',
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativadade', models.ManyToManyField(to='hackathon.Atividade', verbose_name='Atividade')),
                ('hospedagem', models.ManyToManyField(to='hackathon.Hospedagem', verbose_name='Hospedagem')),
                ('restaurante', models.ManyToManyField(to='hackathon.Restaurante', verbose_name='Restaurante')),
            ],
        ),
    ]