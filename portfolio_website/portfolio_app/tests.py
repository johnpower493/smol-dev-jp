from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Project.objects.create(title='Test Project', description='This is a test project', technology='Python', image='img.jpg')

    def test_title_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.title}'
        self.assertEquals(expected_object_name, 'Test Project')

    def test_description_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.description}'
        self.assertEquals(expected_object_name, 'This is a test project')

    def test_technology_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.technology}'
        self.assertEquals(expected_object_name, 'Python')

    def test_image_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.image}'
        self.assertEquals(expected_object_name, 'img.jpg')