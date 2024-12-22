from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post


class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post_data = {
            "username": "testuser",
            "title": "Test Title",
            "content": "Test Content",
        }
        self.post = Post.objects.create(**self.post_data)

    def test_create_post(self):
        response = self.client.post("/careers/", self.post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_get_posts(self):
        response = self.client.get("/careers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_post(self):
        response = self.client.get(f"/careers/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Title")

    def test_update_post(self):
        update_data = {"title": "Updated Title", "content": "Updated Content"}
        response = self.client.patch(
            f"/careers/{self.post.id}/", update_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_post(self):
        response = self.client.delete(f"/careers/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
