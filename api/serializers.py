from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['id','username']



    