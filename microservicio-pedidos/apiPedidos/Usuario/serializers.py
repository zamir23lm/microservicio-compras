# apiPedidos/Usuario/serializers.py

from rest_framework import serializers
from apiPedidos.Usuario.domain.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    idUsuario = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(default="Nombre Predeterminado")
    apellido = serializers.CharField(default="Apellido Predeterminado")
    email = serializers.EmailField(default="ejemplo@correo.com")
    telefono = serializers.CharField(default="123456789", required=False)

    class Meta:
        model = Usuario
        fields = ['idUsuario','nombre', 'apellido', 'email', 'telefono']

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email ya esta registrado")
        return value
    
class UsuarioLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Usuario
        fields = ['email']
    def validate(self, attrs):
        email = attrs.get('email')
        if not Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError("El email no está registrado")
        return attrs

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    class Meta:
        model = Usuario
        fields = ['email']
    def validarEmail(self, value):
        if not Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email no esta registrado")
        return value
    
class TelefonoSerializer(serializers.ModelSerializer):
    telefono = serializers.CharField()
    class Meta:
        model = Usuario
        fields = ['telefono']
    def validate_telefono(self, value):
        if not value.isdigit() or len(value) > 11:
            raise serializers.ValidationError("El número de teléfono es inválido no es digito")
        if len(value) < 8:
            raise serializers.ValidationError("El número de teléfono es inválido")
        return value

