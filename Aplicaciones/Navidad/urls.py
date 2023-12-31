from django.urls import path
from . import views
from .views import pagina, vista, texto, libro, cuaderno, libreta, uno, dos, tres, cuatro, eve , eve1, eve2, eve3, eve4


urlpatterns=[
    path('',views.home),
    path('mostrar/',pagina, name='pagina'),
    path('mostrar1/',texto, name='texto'),
    path('mostrar2/',libro, name='libro'),
    path('mostrar3/',cuaderno, name='cuaderno'),
    path('mostrar4/',libreta, name='libreta'),
    path('mostrar5/',vista, name='vista'),
    path('mostrar6/',uno, name='uno'),
    path('mostrar7/',dos, name='dos'),
    path('mostrar8/',tres, name='tres'),
    path('mostrar9/',cuatro, name='cuatro'),
    path('mostrar10/',eve, name='eve'),
    path('mostrar11/',eve1, name='eve1'),
    path('mostrar12/',eve2, name='eve2'),
    path('mostrar13/',eve3, name='eve3'),
    path('mostrar14/',eve4, name='eve4')

]
