# apiPedidos/Pedido/migrations/0001_initial.py

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True
    dependencies = [
        ('Usuario', '0001_initial'),  # Asegúrate de que 'Usuario' sea la dependencia correcta
        ('DireccionEnvio', '0001_manual_initial'),  # Asegúrate de que 'DireccionEnvio' sea la dependencia correcta
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedidoId', models.AutoField(primary_key=True)),
                ('fechaPedido', models.DateTimeField(auto_now_add=True)),
                ('fechaEntrega', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(max_length=50)),
                ('total', models.DecimalField(max_digits=9, decimal_places=2)),
                ('observaciones', models.CharField(max_length=500, blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='Usuario.Usuario')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='DireccionEnvio.DireccionEnvio')),
            ],
        ),
    ]
