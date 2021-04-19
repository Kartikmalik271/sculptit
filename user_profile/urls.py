from django.urls import path, include
from .views import GetUserProfileView, UpdateUserProfileView, PostArticleList, GetArticleList, UserArticleDetails, GetAllArticleList
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('user',GetUserProfileView.as_view()),
    path('update',UpdateUserProfileView.as_view()),
    path('postarticle', PostArticleList.as_view()),
    path('getarticle', GetArticleList.as_view()),
    path('getallarticle', GetAllArticleList.as_view()),
    path('updatearticle/<int:id>', UserArticleDetails.as_view()),


]
