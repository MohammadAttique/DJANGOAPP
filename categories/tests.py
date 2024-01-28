from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import Category

class CategoryTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Tablets')

    # create
    def test_create_category(self):
        url = reverse('category-list')  # Use reverse to get the URL by name
        data = {'name': 'AC'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        categories = Category.objects.all()
        self.assertEqual(categories[1].name, 'AC')

    # get all
    def test_get_categories(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_category(self):
        url = reverse('category-detail', args=[self.category.id])
        data = {'name': 'Updated Tablets'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(id=self.category.id).name,
                         'Updated Tablets')

    # delete
    def test_delete_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    # additional test 1
    def test_get_category_detail(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tablets')

    # additional test 2
    def test_create_category_without_name(self):
        url = reverse('category-list')
        data = {}  # Missing 'name' field
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # additional test 3
    def test_update_category_invalid_id(self):
        url = reverse('category-detail', args=[999])  # Non-existent ID
        data = {'name': 'Invalid Update'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # additional test 4
    def test_delete_nonexistent_category(self):
        url = reverse('category-detail', args=[999])  # Non-existent ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
