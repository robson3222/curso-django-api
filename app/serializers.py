from app.models import Todo


from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [ 'id', 'nome', 'obs', 'cadastrado', 'finalizado_done']