from django.test import TestCase

class HomePageTest(TestCase):
    def templateTest(self):
        response = self.client.get('/')
        self.assertTemplateUsed('home.html')
