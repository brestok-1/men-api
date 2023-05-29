from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import *

from men.permissions import *
from men.models import Men, Category
from men.serializers import MenSerializer


#
# class MenViewSet(viewsets.ModelViewSet):
#     # queryset = Men.objects.all()  # for get
#     serializer_class = MenSerializer  # for post
#
#     @action(methods=['get'], detail=True)  # false - get list of objects, True - defined objects
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         # return Response({'cats': [c.name for c in cats]})
#         return Response({'cats': cats.name})
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Men.objects.all()
#         return Men.objects.filter(pk=pk)  # we use filter because query_set have to return list

class MenAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()  # for get
    serializer_class = MenSerializer  # for post
    permission_classes = (IsAuthenticatedOrReadOnly,)  # if user doesn't auth, he can only read info, not modify
    pagination_class = MenAPIListPagination

class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)  # access will be granted to users with a token


#
class MenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly,)  # Only admin can delete objects
#

# class MenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer

# class MenApiView(APIView):
#     def get(self, request):
#         lst = Men.objects.all()
#         return Response(
#             {"post": MenSerializer(lst, many=True).data})  # many - serializer should to handle greater than one str
#
#     def post(self, request):
#         serializer = MenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'erros': "Method PUT not allowed"})
#         try:
#             instance = Men.objects.get(pk=pk)
#         except:
#             return Response({'erros': "Objects doesn't exist"})
#
#         serializer = MenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
