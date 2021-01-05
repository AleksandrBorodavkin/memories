from unittest import TestCase

from django.contrib.auth import get_user_model
from django.test import Client

from mem_notes.models import Memories


class MemoriesDetailViewTest(TestCase):

    def setUp(self, ):
        self.client = Client()
        self.user = get_user_model().objects.create(username='test3')
        self.mem_note = Memories.objects.create(subject='test',
                                                description='test',
                                                city='city',
                                                location='',
                                                owner=self.user)

    def test_detail_view(self):
        response = self.client.get('https://localhost:8000/note_detail/' + str(self.mem_note.id) + '/')
        self.assertEqual(response.status_code, 200)
        print('test_view_detail is ok')


class MemoriesListViewTest(TestCase):

    def setUp(self, ):
        self.client = Client()

    def test_list_view(self):
        response = self.client.get('https://localhost:8000/')
        self.assertEqual(response.status_code, 200)
        print('test_view_list is ok')
