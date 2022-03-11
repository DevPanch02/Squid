# Generated by Django 3.2 on 2022-03-10 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usersquid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('registro', models.DateTimeField(auto_now_add=True, verbose_name='Registrado el')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
                ('accedio', models.DateTimeField(blank=True, null=True, verbose_name='último inicio de sesión')),
                ('estado', models.CharField(choices=[('1', 'activo'), ('0', 'inactivo')], default=1, max_length=20, verbose_name='Estado')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'un usuario',
                'verbose_name_plural': 'varios usuarios',
                'db_table': 'usersquid',
                'ordering': ['id'],
            },
        ),
    ]