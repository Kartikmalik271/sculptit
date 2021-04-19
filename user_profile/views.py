from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import UserProfile, UserArticle
from .serializers import UserProfileSerializer, UserArticleSerializer
from rest_framework.decorators import api_view



# Create your views here.
class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username=user.username

            user= User.objects.get(id=user.id)

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile':user_profile.data, 'username':str(username)})
        except:
            return Response({'error':'something went wrong'})

class UpdateUserProfileView(APIView):
    def put(self, request,format=None):
        try:
            user = self.request.user
            username = user.username

            data= self.request.data

            first_name = data['first_name']
            lastt_name = data['lastt_name']
            phone = data['phone']
            college = data['college']
            status=data['status']
            city=data['city']
            linkedin=data['linkedin']
            email=data['email']
            about=data['about']
            we1=data['we1']
            wed1=data['wed1']
            wel11=data['wel11']
            wep12=data['wep12']
            wep13=data['wep13']
            wep14=data['wep14']
            wep15=data['wep15']
            we2=data['we2']
            wed2=data['wed2']
            wel21=data['wel21']
            wep22=data['wep22']
            wep23=data['wep23']
            wep24=data['wep24']
            wep25=data['wep25']
            we3=data['we3']
            wed3=data['wed3']
            wel31=data['wel31']
            wep32=data['wep32']
            wep33=data['wep33']
            wep34=data['wep34']
            wep35=data['wep35']
            class10=data['class10']
            class10marks=data['class10marks']
            class12=data['class12']
            class12marks=data['class12marks']
            collegemarks=data['collegemarks']
            skill1=data['skill1']
            skill2=data['skill2']
            skill3=data['skill3']
            skill4=data['skill4']
            skill5=data['skill5']
            skill6=data['skill6']
            skill7=data['skill7']
            skill8=data['skill8']
            skill9=data['skill9']
            skill10=data['skill10']
            hna1=data['hna1']
            hna2=data['hna2']
            hna3=data['hna3']
            hna4=data['hna4']
            hna5=data['hna5']
            lang1=data['lang1']
            lang2=data['lang2']
            lang3=data['lang3']
            lang4=data['lang4']
            lang1p=data['lang1p']
            lang2p=data['lang2p']
            lang3p=data['lang3p']
            lang4p=data['lang4p']
    

            user= User.objects.get(id=user.id)

            UserProfile.objects.filter(user=user).update(first_name=first_name, lastt_name=lastt_name, phone=phone, college=college,status=status,city=city,linkedin=linkedin,email=email,about=about,we1=we1,wed1=wed1,wel11=wel11,wep12=wep12,wep13=wep13,wep14=wep13,wep15=wep15,we2=we2,wed2=wed2,wel21=wel21,wep22=wep22,wep23=wep23,wep24=wep24,wep25=wep25,we3=we3,wed3=wed3,wel31=wel31,wep32=wep32,wep33=wep33,wep34=wep34,wep35=wep35,class10=class10,class10marks=class10marks,class12=class12,class12marks=class12marks,collegemarks=collegemarks,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,skill5=skill5,skill6=skill6,skill7=skill7,skill8=skill8,skill9=skill9,skill10=skill10,hna1=hna1,hna2=hna2,hna3=hna3,hna4=hna4,hna5=hna5,lang1=lang1,lang2=lang2,lang3=lang3,lang4=lang4,lang1p=lang1p,lang2p=lang2p,lang3p=lang3p,lang4p=lang4p)
            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile':user_profile.data, 'username':str(username)})
        except:
            return Response({'error':'something went wrong'})

class GetArticleList(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username=user.username
            
            author= User.objects.get(id=user.id)
            user_article = UserArticle.objects.filter(user=user.id)
            user_article = UserArticleSerializer(user_article, many=True)

            return Response(user_article.data )
        except:
            return Response({'error':'something went wrong'})

class GetAllArticleList(APIView):
    def get(self, request, format=None):
        try:
           
           
            user_article = UserArticle.objects.all()
            user_article = UserArticleSerializer(user_article, many=True)

            return Response(user_article.data)
        except:
            return Response({'error':'something went wrong'})

class PostArticleList(APIView):
    def post(self, request,format=None):
        try:
            user = self.request.user

            data= self.request.data

            title = data['title']
            contenttype = data['contenttype']
            description = data['description']
            look = data['look']
            user= User.objects.get(id=user.id)
            writer = User.objects.get(username=user.username)
            article_list=UserArticle(user=user, title=title, contenttype=contenttype, description=description, look=look, writer=writer)
            article_list.save()

            user_article = UserArticleSerializer(article_list)

            return Response(user_article.data)
        except:
            return Response({'error':'something went wrong'})


class UserArticleDetails(APIView):
    def get_object(self, id):
        try:
            return UserArticle.objects.get(id=id)
        except UserArticle.DoesNotExist:
            return Response({'error':'something went wrong'})
    
    def get(self ,request, id):
        try:
            articles = self.get_object(id)
            serializer = UserArticleSerializer(articles)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
    
    def put(self ,request, id):
        try:    
            data= self.request.data
            title = data['title']
            contenttype = data['contenttype']
            description = data['description']
            look = data['look']
            
            UserArticle.objects.filter(id=id).update(title=title, contenttype=contenttype, description=description, look=look)
            articles = self.get_object(id)
            serializer = UserArticleSerializer(articles)

            return Response(serializer.data)
        except:
            return Response({'error':'something went wrong'})


    def delete(self, request, id):
        articles = self.get_object(id)
        articles.delete()     
        
           
        return Response({'success':'deleted'})
       

