from django.urls import path

from . import views

app_name = 'plataforma'

urlpatterns = [
    path('', views.plataforma, name="home"),
    path('escolas/', views.escolas, name="escolas"),
    path('responsaveis/', views.responsaveis, name="responsaveis"),
    path('alunos/', views.alunos, name="alunos"),
    path('transportadores/', views.transportadores, name="transportadores"),
    path('localizacao', views.localizacao, name="localizacao"),
    path('escolas_parceiras', views.escolas_parceiras, name="escolas_parceiras"),
    path('consultar_transportadores', views.consultar_transportadores, name="consultar_transportadores"),

] 