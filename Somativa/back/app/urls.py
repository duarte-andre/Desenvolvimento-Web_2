from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuarioCustomizadoView)
router.register(r'categorias', CategoriaView)
router.register(r'livros', LivroView)
router.register(r'emprestimos', EmprestimoView)


urlpatterns = router.urls
