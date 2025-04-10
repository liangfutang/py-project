from django.urls import path
from . import views
from .views import BookView

urlpatterns = [
    path('test/', views.orm_select),
    path('book/', BookView.as_view(), name='book'),
]
