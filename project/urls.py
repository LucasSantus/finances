from django.contrib import admin
from django.urls import path
from dashboard.views import index
from movimentacoes.views import criar_movimentacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('criar-movimentacao/', criar_movimentacao, name="criar_movimentacao")
]
