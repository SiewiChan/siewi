from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView,ArticleView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('<category>/<int:tutorial_pk>',ArticleView.as_view(),name='article'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
