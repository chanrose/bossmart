from django.test import TestCase
from django.contrib.auth.models import User
# from apps.order import Order
from django.urls import reverse

class UserTestCase(TestCase):

    def test_registration(self):
        response = self.client.get(reverse('customer:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oscar/customer/registration.html')
        response = self.client.post(reverse('customer:register'), {'username': 'kate', 'password': 'kate123', 'email': 'kate@gmail.com'})
        self.assertEquals(response.status_code, 200)

    def test_authentication(self):
        response = self.client.get(reverse('customer:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oscar/customer/login_registration.html')
        user = User.objects.get(username='kate')    
        response = self.client.login(username=user.username, password=user.password)
        self.assertEquals(response.status_code, 200)

    def test_update_password(self):
        response = self.client.post(reverse('customer:change-password'), {'username': 'kate', 'password': 'kate123', 'email': 'kate@gmail.com'})
# class OrderTestCase(TestCase):
#     def test_create_order(self):
#         # Order.objects.create()
#         pass
        
