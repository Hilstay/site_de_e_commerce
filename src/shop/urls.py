from django.urls import path
from .views import index, detail, register, connexion, deconnexion, add_to_cart, cart, delete, avertissement
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name="index"),
    path('<int:myid>', detail, name="detail"),
    path('register/', register, name="register"),
    path('login/', connexion, name="login"),
    path('logout/', deconnexion, name="logout"),
    path('add-to-cart/<int:myid>', add_to_cart, name="add-to-cart"),
    path('cart/', cart, name='cart'),
    path('delete/', delete, name='delete'),
    path('erreur/', avertissement, name="erreur")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)