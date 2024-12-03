from django.urls import path
from .views import chat_view,generate_code
from . import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_view, name='chat'),
    path('generate-code/', views.generate_code, name='generate-code'),
]
