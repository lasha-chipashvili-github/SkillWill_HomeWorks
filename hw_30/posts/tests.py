from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Post

# %% 2

"""
    Test that the model can be saved to the database.
    Test that the model can be retrieved from the database.
    Test that the model can be updated in the database.
    Test that the model can be deleted from the database.
"""


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


# %% 3
"""
    Test that the view returns a status code of 200.
    Test that the view returns a queryset of all the objects.
    Test that the view returns the correct template.
"""

class PostApiTest(APITestCase):
    """
    ვინაიდან ამ შემთხვევაში generic ვიუ მაქვს გამოყენებული, template-ს შემოწმება არ გამომივიდა,
    თუმცა იმავეს დავალების სხვა ნაწილში ვაკეთებ.
    """

    @classmethod
    def setUpTestData(cls):
        """
             სატესტო მონაცემების შექმნა კლასის დონეზე
        """
        cls.post1 = Post.objects.create(
            title="Post1",
            body="Body1"
        )

        cls.post2 = Post.objects.create(
            title="Post2",
            body="Body2"
        )

    def test_api_listview(self):
        response = self.client.get(reverse("post_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 2)
        self.assertContains(response, self.post1)


#       self.assertTemplateUsed(response, 'posts/post_list.thml')

#%% 4

"""
    Test that the form is valid with correct data.
    Test that the form is invalid with incorrect data.
"""

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


# %% 5

"""
    Test that the view returns a status code of 200.
    Test that the view updates the object correctly.
    Test that the view returns the correct template.
"""

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


# %% 6
"""
    Test that the view returns a status code of 302 (redirect).
    Test that the view deletes the object correctly.
"""


class DeletePostViewTest(TestCase):
    def setUp(self):
        self.obj = Post.objects.create(title="Test Post", body="Test Body")

    def test_view_returns_302(self):
        response = self.client.get(reverse('post_delete', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 302)

    def test_view_deletes_object_correctly(self):
        response = self.client.get(reverse('post_delete', args=[self.obj.pk]))
        self.assertEqual(Post.objects.count(), 0)
