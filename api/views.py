from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Aluno, Curso, Inscricao
from .serializers import AlunoSerializer, CursoSerializer, InscricaoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

