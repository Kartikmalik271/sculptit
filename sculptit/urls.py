from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

urlpatterns = [
   path('api/',include('rest_framework.urls')),
   path('account/',include('api.urls')),
   path('profile/',include('user_profile.urls')),
   re_path('.*', TemplateView.as_view(template_name='index.html'))
]


