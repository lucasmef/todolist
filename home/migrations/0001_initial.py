# Generated by Django 5.2.4 on 2025-07-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_conclusao', models.DateTimeField(blank=True, null=True)),
                ('concluido', models.BooleanField(default=False)),
            ],
        ),
    ]
