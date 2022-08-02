from rest_framework.routers import DefaultRouter
from api.views import AlunoViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)

router.register(r'alunos', AlunoViewSet)

urlpatterns = router.urls