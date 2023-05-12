from .models import Category, Product
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase



# Create your tests here.
class ProductApiTestCase(APITestCase):

    def setUp(self):
        testCategory = Category(name="Test Category")
        testCategory.save()
        testProduct = Product(name="Test Product",price =19.99, category = testCategory)
        testProduct.save()
        self.client = APIClient()
    
    def test_models_setup(self):
        '''
        Test create Product, Category
        '''
        self.assertEqual(Product.objects.get().name, "Test Product")
        self.assertEqual(Category.objects.get().name, "Test Category")
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Category.objects.count(), 1)


    def test_get_latest_products(self):
        '''
        Test get latest-products endpoint
        '''

        # response = self.client.get("http://127.0.0.1:8000/api/v1/latest-products/")
        response = self.client.get(reverse('latest-products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)





