```python
from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Project.objects.create(title='First Project', description='This is a description', technology='Django', image='img.jpg')

    def test_title_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.title}'
        self.assertEquals(expected_object_name, 'First Project')

    def test_description_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.description}'
        self.assertEquals(expected_object_name, 'This is a description')

    def test_technology_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.technology}'
        self.assertEquals(expected_object_name, 'Django')

    def test_image_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.image}'
        self.assertEquals(expected_object_name, 'img.jpg')
```