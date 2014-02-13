from rest_framework import serializers

from todo.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.Field('owner.username')

    class Meta:
        model = Tasks
        fields = ('title', 'description', 'completed', 'owner')