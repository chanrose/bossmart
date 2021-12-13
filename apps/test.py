from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.test.client import RequestFactory, Client
# from apps.order import Order
from django.urls import reverse

class UserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='kate', email='kate@gmail.com')
        self.user.set_password('kate123')
        self.user.save()

    def test_registration(self):    
        response = self.client.get(reverse('customer:register'))
        self.assertIsNotNone(self.user)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'oscar/customer/registration.html')    

    def test_authentication(self):
        response = self.client.get(reverse('customer:login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'oscar/customer/login_registration.html')
        self.user = User.objects.get(username='kate') 
        self.assertIsNotNone(self.user)  
        self.user = authenticate(username='kate', password='kate123')
        self.assertTrue(self.user.is_authenticated)
    
    def test_login(self):
        user = self.client.login(username='kate', password='kate123')
        self.assertEqual(user, not None)

    def test_logout(self):
        user = self.client.logout()
        self.assertEqual(user, None)

    def test_update_password(self):
        response = self.client.get(reverse('customer:change-password'))
        self.assertEquals(response.status_code, 302)
        # response = self.client.post(reverse('customer:change-password'), {'password': 'kate1234', 'email': 'kate@gmail.com'})
        # self.assertEquals(response.status_code, 200)

class ProfileTestCase(TestCase):

    def test_update_profile(self):
        # response = self.client.get(reverse('customer:profile-update'), follow=True)
        # self.assertEquals(response.status_code, 200)
        response = self.client.post(reverse('customer:profile-update'), {'first_name': 'jane', 'last_name': 'maylor'}, follow=True)
        self.assertEquals(response.status_code, 200)
        # self.client(reverse('customer:profile-view'), {})
        # self.assertTemplateUsed(response, 'oscar/customer/profile_form.html')
        

# class OrderTestCase(TestCase):
#     def test_create_order(self):
#         # Order.objects.create()
#         pass
        
