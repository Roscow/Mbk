# Generated by Django 2.1.2 on 2018-10-29 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_delete_cuenta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('usuario', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=50)),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
    ]