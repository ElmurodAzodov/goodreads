from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
  
# Create your tests here.

class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "JohnDoe", 
                "first_name": "John", 
                "last_name": "Doe", 
                "email": "johndoe@gmail.com", 
                "password": "qweqwe123"
                }
        )
  
        user = User.objects.get(username="JohnDoe")

        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "johndoe@gmail.com")
        self.assertNotEqual(user.password ,"qweqwe123")
        self.assertTrue(user.check_password("qweqwe123"))


    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "John",
                "email": "johndoe@gmail.com"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")
        

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "johndoe",
                "first_name": "John",
                "last_name": "Doe",
                "email": "invalid_email",
                "password": "qweqwe123"
            }
        )
        
        user_count = User.objects.all()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")
    
    def test_unique_username(self):
        user = User.objects.create(username="j") 