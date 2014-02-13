from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from todo.models import Tasks
from api.serializers import TaskSerializer
from api.permissions import IsOwnerOrReadOnly

class TaskMixin(object):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permissions_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class TaskViewSet(TaskMixin, viewsets.ModelViewSet):
    pass


task_router = DefaultRouter
task_router.register(r'tasks', TaskViewSet)