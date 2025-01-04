from django.urls import include, path
from testing.views import CrossrefView

urlpatterns = [
    path('unicorn/', include('django_unicorn.urls')),
    path('', CrossrefView.as_view(), name='movies')
]
