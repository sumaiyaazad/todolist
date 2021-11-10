from rest_framework.serializers import ModelSerializer

from .models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'desc', 'is_complete',)
        # fields = '__all__'
        # read_only_fields = ['owner']