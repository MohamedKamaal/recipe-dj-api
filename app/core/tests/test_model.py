from django.db.utils import IntegrityError
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# Create your tests here.

class UserCreatingTests(TestCase):
    """ test creating user object in different scenarios"""
    
    
    def test_valid_email_valid_password_no_username_pass(self):
        """test creating a new user with valid email address"""
        
        #data to create_user new user 
        email = "moka@gmail.com"
        password = "password12345"
        
        #creating new user object 
        user = get_user_model().objects.create_user(email=email, password=password)
        
        #checking if email was saved 
        self.assertEqual(user.email, email)
        
        #checking if password was hashed and saved 
        self.assertTrue(user.check_password(password))
        
    
    def test_create_user_invalid_emails_fail(self):
        """ test creting user with invalid email"""
        
        #data to ceate new user 
        emails = ["mokfgmail.com","moka@dgdg@yahoo.com","@sgfgd.com","mokas"]
        password = "1235ye4pass"
        
        #creating new user 
        for email in emails: 
            with self.subTest(email=email):
                with self.assertRaises(ValidationError):
                    user = get_user_model().objects.create_user(email=email, password=password)
        
        #checking if user is created 
        self.assertEqual(get_user_model().objects.count(),0)
    
    def test_create_user_uppercase_domain_part_pass(self):
        """ test for handling not normalized email """
        user_data = {
            'email':'muhamed@YAHOO.COM',
            'password':'passwortyd13435'
        }
        user = get_user_model().objects.create_user(**user_data)
        
        #checking if lowering occured
        self.assertEqual(user.email, user_data['email'].lower())
    
    def test_user_creatiion_short_password_fail(self):
        """ test creating user with short password"""
        
        # creating user data 
        email = 'moka@outlook.com'
        password = "1"
        
        # creating user object
        
        # Integrity error should be raises
        with self.assertRaises(ValidationError):
            user = get_user_model().objects.create_user(email=email, password=password)
        
        
    def test_create_user_no_email_fail(self):
        """ test creating user with no email but username"""
        
        # creating user data 
        username = 'moka'
        password = "12htth3password"
        
        # creating user object
        
        with self.assertRaises(TypeError):
            user = get_user_model().objects.create_user(username=username, password=password)
        
    
    
    def test_creating_user_duplicate_emails_fail(self):
        """ test creating two users with same email"""
        # user data 
        user1_info ={
            'email':'moka@outlook.com',
            'password':'pass1ghkhg23'
        }
        
        # create two user objects with same email
        user1 = get_user_model().objects.create_user(**user1_info)
        with self.assertRaises(IntegrityError):
            user2 = get_user_model().objects.create_user(**user1_info)

        # checking numb er of user objects
        self.assertEqual(get_user_model().objects.count(),1)
    
    def test_create_user_missing_email_fail(self):
        """ create user without email """
        # user data 
        user_data = {
            'password':'passwgfjord123'
        }
        
        # validation error should arise
        with self.assertRaises(TypeError):
            user = get_user_model().objects.create_user(**user_data)
    
    
    def test_create_superuser_pass(self):
        """ create superuser """

        user_data = {
            'email':'moka@outlook.com',
            'password':'rfshfshhfsf'
        }

        user = get_user_model().objects.create_superuser(**user_data)

        self.assertTrue(user.is_superuser)