from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime

# Create your tests here.
class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.welcome_url = reverse('welcome')
        self.hi_url = reverse('hi', args=['John'])
        self.day_url = reverse('day', args=['1990-12-26'])
        self.compare_url = reverse('compareAge', args=['2001-01-01', '2000-01-01'])
        self.greather_url = reverse('greatherAge', args=['1989-12-26', '1990-12-26'])
        self.start_sign_url = reverse('star_sign', args=[19,1])
    
    def test_welcome(self):
        response = self.client.get(self.welcome_url)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<h1>Welcome to the CI/CD testing app!</h1>')
        self.assertContains(response, '<li>Go to the /hi/name page to say hi to your name.</li>')
        self.assertContains(response, '<li>Go to the /day/date page to get your age. Format AAAA-MM-DD, example: /day/1990-12-26 </li>')
        
    def test_hi(self):
        response = self.client.get(self.hi_url)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Hello John! Welcome to the CI/CD testing app.')
    
    def test_day(self):
        response = self.client.get(self.day_url)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'You are 32 years old.')
        
    def test_compareAge(self):
        response = self.client.get(self.compare_url)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'The difference of age is 1 years.')
        
    def test_greatherAge(self):
        response = self.client.get(self.greather_url)
       
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'The greather age is 1989-12-26 00:00:00 years.')
        
    def test_start_sign(self):
        response = self.client.get(self.start_sign_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Capricornio')