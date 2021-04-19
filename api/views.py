from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from user_profile.models import UserProfile
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import auth
from .serializers import UserSerializer


class CheckAuthenticatedView(APIView):
    def get(self, request,format=None):
        user=self.request.user

        try:
            isAuthenticated = User.is_authenticated
            
            if isAuthenticated:
                return Response({'isAuthenticated':'success'} )
            else:
                return Response({'isAuthenticated':'error'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']
        re_password = data['re_password']


        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({'error':'username already exists'})
                else:
                    if len(password)< 6:
                        return Response({'error':'password  too short'})
                    else:
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        user = User.objects.get(id=user.id)
                        user_profile= UserProfile(user=user ,first_name='', lastt_name='',phone='',college='',status='',city='',linkedin='',email='',about='',we1='',wed1='',wel11='',wep12='',wep13='',wep14='',wep15='',we2='',wed2='',wel21='',wep22='',wep23='',wep24='',wep25='',we3='',wed3='',wel31='',wep32='',wep33='',wep34='',wep35='',class10='',class10marks='',class12='',class12marks='',collegemarks='',skill1='',skill2='',skill3='',skill4='',skill5='',skill6='',skill7='',skill8='',skill9='',skill10='',hna1='',hna2='',hna3='',hna4='',hna5='',lang1='',lang2='',lang3='',lang4='',lang1p='',lang2p='',lang3p='',lang4p='')
                        user_profile.save()

                        return Response({'success':'user created successfully'})
            else:
                return Response({'error':'Passwords do not match'})
        except:
            return Response({'error':'something went wrong'})

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes= (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username= data['username']
        password= data['password']

        try:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({'success':'logged in'})
            else:
                return Response({'error':'authentication error'})
        except:
            return Response({'error':'something went wrong'})

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success':'loggedOut successfully'})
        except:
            return Response({'error':'something went wrong'})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success':'CSRF cookie set'})


class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data) 