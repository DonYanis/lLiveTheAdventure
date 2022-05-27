
from django.db import models
from django.contrib.auth.models import AbstractUser




    
status_choice=(('Simple','SIMPLE'),('Adherant','ADHERENT'),('Fidele','FIDELE'))

class User(AbstractUser):
    is_admin=models.BooleanField(default='False')
    is_client=models.BooleanField(default='True')

    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(unique=True,null=True)
    phonenumber=models.CharField(max_length=20, null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    avatar=models.ImageField(null=True,blank=True)
    status=models.CharField(max_length=14,choices=status_choice,default='Simple')
    points=models.IntegerField(null=True,blank=True,default=0)
    has_avatar=models.BooleanField(default='False')

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]


class TripType(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Trip(models.Model):
    type=models.ForeignKey(TripType,on_delete=models.SET_NULL,null=True)
    
    waitinglist=models.ManyToManyField(User,related_name='participants',blank=True)
    participants=models.ManyToManyField(User,related_name='waitinglist',blank=True)
    
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000,null=True,blank=True)
    level=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    total_places=models.IntegerField(null=True,blank=True)
    taken_places=models.IntegerField(null=True,default=0)
    left_places=models.IntegerField(null=True,blank=True)
    program=models.TextField(max_length=2000,default='')
    prevoir=models.TextField(max_length=1000,default='')
    prixComprend=models.TextField(max_length=1000,default='')
    depart_place=models.CharField(max_length=200)
    blog_link=models.URLField(null=True, max_length=300,db_index=True,blank=True)
    active=models.BooleanField(default='True')
    depart=models.DateTimeField(blank='True')
    retour=models.DateTimeField(blank='True')
    is_closed=models.BooleanField(default='False')
    month_name=models.CharField(max_length=12,default='')

    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS=['name','type','level','price']
    class Meta:
        ordering=['-updated','-created']
    def __str__(self):
        return str(self.name)



   
class Blog(models.Model):
    name=models.CharField(max_length=200)
    main_image=models.ImageField(null=True,default="avatar.svg")

    main_section=models.TextField(max_length=3000,null=True,blank=True)
    section2_title=models.CharField(max_length=3000,null=True,blank=True)
    section2=models.TextField(max_length=3000,null=True,blank=True)
    section2_image=models.ImageField(null=True,default="avatar.svg")
    section3_title=models.CharField(max_length=3000,null=True,blank=True)
    section3=models.TextField(max_length=3000,null=True,blank=True)
    section3_image=models.ImageField(null=True,default="avatar.svg")
    section4_title=models.CharField(max_length=3000,null=True,blank=True)
    section4=models.TextField(max_length=3000,null=True,blank=True)
    section4_image=models.ImageField(null=True,default="avatar.svg")
    section5_title=models.CharField(max_length=3000,null=True,blank=True)
    section5=models.TextField(max_length=3000,null=True,blank=True)
    section5_image=models.ImageField(null=True,default="avatar.svg")
    
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-updated','-created']
    def __str__(self):
        return str(self.section1[0:50])


class TripImage(models.Model):
    avatar=models.ImageField(null=True,default="avatar.svg")
    trip=models.ForeignKey(Trip,on_delete=models.SET_NULL,null=True)


class Notification(models.Model):
    name=models.CharField(max_length=50)
    body=models.TextField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    

    created=models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS=['name','body']

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.name

class FeedBack(models.Model):
    rate=models.IntegerField()
    body=models.TextField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    is_accepted=models.BooleanField(default='False')

    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-rate']

    def __str__(self):
        return self.body

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username