from django.urls import path
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

from app_ingressos import views

urlpatterns = [
    path('', RedirectView.as_view(url='admin/')),
    # Get all Calls in Progress
    path(
        'shows', views.shows,
        name='shows'
        ),
    path(
        'show-financial/<str:show_id>/', views.show_financial,
        name='show_financial'
        ),
]
urlpatterns = format_suffix_patterns(urlpatterns)