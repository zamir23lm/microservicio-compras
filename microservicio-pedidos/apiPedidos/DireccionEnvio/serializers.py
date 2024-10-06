# serializers.py
from rest_framework import serializers
from apiPedidos.Usuario.domain.models import Usuario
from apiPedidos.DireccionEnvio.domain.models import DireccionEnvio

class DireccionEnvioSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    direccionId = serializers.IntegerField(required=False)
    class Meta:
        model = DireccionEnvio
        fields = [
            'direccionId', 'usuario', 'direccion', 'distrito', 'provincia',
            'departamento', 'pais', 'codigoPostal', 'instrucciones', 'latitud', 'longitud'
        ]

class EditDIreccionSerializer(serializers.ModelSerializer):
    direccion = serializers.CharField(required=True, max_length=300)
    distrito = serializers.CharField(required=False, allow_blank=True, max_length=50)
    provincia = serializers.CharField(required=False, allow_blank=True, max_length=50)
    departamento = serializers.CharField(required=True, max_length=50)
    pais = serializers.CharField(required=True, max_length=50)
    codigoPostal = serializers.CharField(required=False, allow_blank=True, max_length=10)
    instrucciones = serializers.CharField(required=False, allow_blank=True, max_length=500)
    latitud = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitud = serializers.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        model = DireccionEnvio
        fields = [
            'direccion', 'distrito', 'provincia',
            'departamento', 'pais', 'codigoPostal', 'instrucciones', 'latitud', 'longitud'
        ]
        
class DirecciondtoSerializer(serializers.ModelSerializer):
    direccionId = serializers.IntegerField()
    usuario = serializers.IntegerField()
    direccion = serializers.CharField()
    distrito = serializers.CharField()
    provincia = serializers.CharField()
    departamento = serializers.CharField()
    pais = serializers.CharField()
    codigoPostal = serializers.CharField()
    instrucciones = serializers.CharField()
    latitud = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitud = serializers.DecimalField(max_digits=9, decimal_places=6)
    class Meta:
        model = DireccionEnvio
        fields = [
            'direccionId', 'usuario', 'direccion', 'distrito', 'provincia',
            'departamento', 'pais', 'codigoPostal', 'instrucciones', 'latitud', 'longitud'
        ]
class UpdateDireccionSerializer(serializers.ModelSerializer):
    direccion = serializers.CharField(required=False, max_length=300)
    distrito = serializers.CharField(required=False, allow_blank=True, max_length=50)
    provincia = serializers.CharField(required=False, allow_blank=True, max_length=50)
    departamento = serializers.CharField(required=False, max_length=50)
    pais = serializers.CharField(required=False, max_length=50)
    codigoPostal = serializers.CharField(required=False, allow_blank=True, max_length=10)
    instrucciones = serializers.CharField(required=False, allow_blank=True, max_length=500)
    latitud = serializers.DecimalField(max_digits=9, decimal_places=6, required=False, allow_null=True)
    longitud = serializers.DecimalField(max_digits=9, decimal_places=6, required=False, allow_null=True)

    class Meta:
        model = DireccionEnvio
        fields = [
            'direccion', 'distrito', 'provincia',
            'departamento', 'pais', 'codigoPostal', 'instrucciones', 'latitud', 'longitud'
        ]