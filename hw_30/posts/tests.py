from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Post

#%% 2
class PostTest(TestCase):
    def setUp(self):
        """
        დროებითი სატესტო ბაზის შექმნა
        """
        self.obj = Post.objects.create(title='Test Post', body='Test Post Body')

    def test_post_save(self):
        """
        დატესტვა იმისა ბაზაში რამდენი ტესტი არსებობს, ანუ შეიქმნა თუ არა პოსტის ობიექტი
        """
        self.assertEqual(Post.objects.count(), 1)

    def test_post_retrieve(self):
        """
        იტესტება რამდენად სწორად ხდება ბაზიდან შექმნილი ტესტის სათაურის წამოღება
        """
        obj = Post.objects.get(id=self.obj.id)
        self.assertEqual(obj.title, 'Test Post')

    def test_post_update(self):
        """
        იტესტება რამდენად ხდება მონაცემის განახლება ბაზაში და შემდგომ მისი ახალი მნიშვნელობით ხელახლა წამოღება
        """
        self.obj.title = 'Updated'
        self.obj.save()
        obj = Post.objects.get(id=self.obj.id)
        self.assertEqual(obj.title, 'Updated')

    def test_post_delete(self):
        """
        იტესტება ხდება თუ არა ბაზაში ელემენტის წაშლა
        """
        self.obj.delete()
        self.assertEqual(Post.objects.count(), 0)

#%% 3


class PostApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post1 = Post.objects.create(
            title="Post1",
            body="Body1"
        )

        cls.post1 = Post.objects.create(
            title="Post2",
            body="Body2"
        )

    def test_api_listview(self):
        response = self.client.get(reverse("post_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 2)
        self.assertContains(response, self.post1)
        self.assertTemplateUsed(response, 'posts/post_list.thml')

# class PostAPIViewTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.post = Post.objects.create(title='Test Post', body='Test Body')
#
#     def test_list_view_status_code(self):
#         response = self.client.get(reverse('post-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_list_view_queryset(self):
#         response = self.client.get(reverse('post-list'))
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['title'], 'Test Post')
#
#     def test_list_view_template(self):
#         response = self.client.get(reverse('post-list'))
#         self.assertEqual(response.accepted_renderer.format, 'json')
#
#     def test_create_view_valid_data(self):
#         data = {'title': 'New Test Post', 'body': 'New Test Body'}
#         response = self.client.post(reverse('post-list'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Post.objects.count(), 2)
#
#     def test_create_view_invalid_data(self):
#         data = {'title': '', 'body': 'Invalid content', 'slug': 'invalid-post'}
#         response = self.client.post(reverse('post-list'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(Post.objects.count(), 1)
#
#     def test_update_view_status_code(self):
#         data = {'title': 'Updated Post', 'body': 'Updated content'}
#         response = self.client.put(reverse('post-detail', args=[self.post.id]), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Post.objects.get(id=self.post.id).title, 'Updated Post')
#
#     def test_update_view_template(self):
#         data = {'title': 'Updated Post', 'body': 'Updated content'}
#         response = self.client.put(reverse('post-detail', args=[self.post.id]), data, format='json')
#         self.assertEqual(response.accepted_renderer.format, 'json')
#
#     def test_delete_view_status_code(self):
#         response = self.client.delete(reverse('post-detail', args=[self.post.id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Post.objects.count(), 0)

#%% 4
from .forms import PostForm
class PostTest(TestCase):
    def test_valid_form(self):
        data = {'title': 'Test Post', 'body': 'Test Body'}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'title': '', 'body': ''}
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())

#%% 5

# myapp/tests.py
class PostUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = Post.objects.create(title='Test Post', body='Test Body')

    def test_view_status_code(self):
        response = self.client.get(reverse('post_update', kwargs={'pk': self.obj.id}))
        self.assertEqual(response.status_code, 200)

    def test_view_update_object(self):
        response = self.client.post(reverse('post_update', kwargs={'pk': self.obj.id}),
                                    {'title': 'Updated Test Post', 'body': 'Updated Test Body'})
        obj = Post.objects.get(id=self.obj.id)
        self.assertEqual(obj.title, 'Updated Test Post')

    def test_view_template(self):
        response = self.client.get(reverse('post_update', kwargs={'pk': self.obj.id}))
        self.assertTemplateUsed(response, 'posts/post_update.html')


#%% 6
class DeletePostViewTest(TestCase):
    def setUp(self):
        self.obj = Post.objects.create(title="Test Post", body="Test Body")

    def test_view_returns_302(self):
        response = self.client.get(reverse('post_delete', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 302)

    def test_view_deletes_object_correctly(self):
        response = self.client.get(reverse('post_delete', args=[self.obj.pk]))
        self.assertEqual(Post.objects.count(), 0)