from rest_framework.routers import DefaultRouter
from api.views import AlunoViewSet


# app_name = 'teste'

router = DefaultRouter(trailing_slash=False)

router.register(r'alunos', AlunoViewSet)
# router.register(r'professor', AlunoViewSet)

urlpatterns = router.urls