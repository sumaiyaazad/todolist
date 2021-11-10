from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from todos.pagination import  CustomPageNumberPagination

# class CreateTodoAPIView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)
#
#
# class TodoListAPIView(ListAPIView):
#     """
#     List all Todos, or create a new todos.
#     """
#
#     serializer_class = TodoSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)


class TodosAPIView(ListCreateAPIView):
    """
    List all Todos, or create a new todos.
    """

    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'desc', 'title', 'is_complete']
    search_fields = ['id', 'desc', 'title', 'is_complete']
    ordering_fields = ['id', 'desc', 'title', 'is_complete']

    def perform_create(self, serializer):

        return serializer.save(owner=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
    #     return super().perform_create(serializer)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a todos instance.
    """
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field="id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
