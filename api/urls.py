from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, CursoViewSet, InscricaoViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'inscricoes', InscricaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
