#Aqui nós estamos apenas importando a função url do Django e todos as nossas views do aplicativo blog
from django.conf.urls import url
from . import views
#Depois disso nós podemos adicionar nosso primeiro padrão de URL
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
