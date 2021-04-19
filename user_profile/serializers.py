from rest_framework import serializers
from .models import UserProfile, UserArticle
from rest_framework.authtoken.views import Token


class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
       model = UserProfile
       fields = '__all__'

class UserArticleSerializer(serializers.ModelSerializer):
   class Meta:
       model = UserArticle
       fields = '__all__'



    