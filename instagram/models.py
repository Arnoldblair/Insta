from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
#Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email,company_name,phone,password=None):
        if not email:
            raise ValueError("email is required")
        if not company_name:
            raise ValueError("company name is required")

        if not phone:
            raise ValueError("please provide an active phone number")

        user=self.model(
        email=self.normalize_email(email),
        company_name=company_name,
        phone=phone
    )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,company_name,phone,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            company_name=company_name,
            phone=phone,
            password=password
        )   
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db) 

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email address", max_length=60,unique=True)
    company_name=models.CharField(verbose_name="company name", max_length=200, unique=True)
    phone=models.CharField(max_length=20,verbose_name="company phone")
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)


    USERNAME_FIELD="email"

    REQUIRED_FIELDS=['company_name', 'phone']

    objects=MyUserManager()

    def __str__(self):
        return self.company_name

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True  


class Profile(models.Model):
    bio = models.CharField(max_length =200)
    profile_pic = CloudinaryField('image')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    followers = models.ManyToManyField('Profile',related_name="profile_followers",blank=True,default=[0])
    following = models.ManyToManyField('Profile',related_name="profile_following",blank=True,default=[0])


    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(user__icontains=search_term)
        return profiles    
        


class Image(models.Model):
    image = CloudinaryField('image')
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name="user_name")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    image_name = models.CharField(max_length =30)
    caption = models.CharField(max_length =50)
    post_date = models.DateTimeField(auto_now_add=True)
            