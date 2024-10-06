# apiPedidos/DireccionEnvio/migrations/0001_initial.py

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0001_initial'),  # Asegúrate de que 'Usuario' es la dependencia correcta
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionEnvio',
            fields=[
                ('direccionId', models.AutoField(primary_key=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direccion_pedido', to='Usuario.Usuario')),
                ('direccion', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('codigoPostal', models.CharField(max_length=10, blank=True, null=True)),
                ('instrucciones', models.CharField(max_length=500, blank=True, null=True)),
                ('latitud', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitud', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
        ),
    ]
