
from math import e
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create User model manager 
class UserManager(BaseUserManager):

    """handle user object creation"""

    def create_user(self, email, password=None, **extra_fields):
        """create new user"""
        
        # password make sure it is long 
        if len(password)<=8:
            raise ValidationError(f'password must be longer than 8')
        # make sure email was sent 
        if not email :
            raise ValidationError('Email is required')

        # validate email 
        try :
            validate_email(email)
        
        except ValidationError:
            raise ValidationError(f'Invalid email: {email}')

        # normalize email
        email = self.normalize_email(email)
        
        
        #create user instance
        user = self.model(email=email, **extra_fields)
        
        # hash pasword and save it 
        user.set_password(password)
        user.save(using = self._db)
        
        return user 

#creating custom user model 
class User(AbstractBaseUser, PermissionsMixin):
    """create custom user"""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length= 255, blank=True, null=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False)
    
    # set UserManager as default manager  
    objects = UserManager()
    
    # set email as required for authentication
    USERNAME_FIELD = 'email'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  