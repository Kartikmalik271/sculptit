from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

def uplaod_path(filename):
    return '/'.join(['profileimg',filename])

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    lastt_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=15, default='')
    college = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    linkedin = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    about = models.CharField(max_length=500, default='')
    we1 = models.CharField(max_length=100, default='')
    wed1 = models.CharField(max_length=100, default='')
    wel11 = models.CharField(max_length=100, default='')
    wep12 = models.CharField(max_length=100, default='')
    wep13 = models.CharField(max_length=100, default='')
    wep14 = models.CharField(max_length=100, default='')
    wep15 = models.CharField(max_length=100, default='')

    we2 = models.CharField(max_length=100, default='')
    wed2 = models.CharField(max_length=100, default='')
    wel21 = models.CharField(max_length=100, default='')
    wep22 = models.CharField(max_length=100, default='')
    wep23 = models.CharField(max_length=100, default='')
    wep24 = models.CharField(max_length=100, default='')
    wep25 = models.CharField(max_length=100, default='')

    we3 = models.CharField(max_length=100, default='')
    wed3 = models.CharField(max_length=100, default='')
    wel31 = models.CharField(max_length=100, default='')
    wep32 = models.CharField(max_length=100, default='')
    wep33 = models.CharField(max_length=100, default='')
    wep34 = models.CharField(max_length=100, default='')
    wep35 = models.CharField(max_length=100, default='')

    class10 = models.CharField(max_length=100, default='')
    class10marks = models.CharField(max_length=100, default='')
    class12 = models.CharField(max_length=100, default='')
    class12marks = models.CharField(max_length=100, default='')
    collegemarks = models.CharField(max_length=100, default='')
    skill1 = models.CharField(max_length=100, default='')
    skill2 = models.CharField(max_length=100, default='')
    skill3 = models.CharField(max_length=100, default='')
    skill4 = models.CharField(max_length=100, default='')
    skill5 = models.CharField(max_length=100, default='')
    skill6 = models.CharField(max_length=100, default='')
    skill7 = models.CharField(max_length=100, default='')
    skill8 = models.CharField(max_length=100, default='')
    skill9 = models.CharField(max_length=100, default='')
    skill10 = models.CharField(max_length=100, default='')
    hna1 = models.CharField(max_length=100, default='')
    hna2 = models.CharField(max_length=100, default='')
    hna3 = models.CharField(max_length=100, default='')
    hna4 = models.CharField(max_length=100, default='')
    hna5 = models.CharField(max_length=100, default='')
    lang1 = models.CharField(max_length=100, default='')
    lang2 = models.CharField(max_length=100, default='')
    lang3 = models.CharField(max_length=100, default='')
    lang4 = models.CharField(max_length=100, default='')
    lang1p = models.CharField(max_length=100, default='')
    lang2p = models.CharField(max_length=100, default='')
    lang3p = models.CharField(max_length=100, default='')
    lang4p = models.CharField(max_length=100, default='')
 



    def __str__(self):
        return self.first_name

class UserArticle(models.Model):
   
    title = models.CharField(max_length=100, default='')
    contenttype = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, default='')
    look = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    writer = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
