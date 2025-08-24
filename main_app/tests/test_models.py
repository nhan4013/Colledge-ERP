from django.test import TestCase
from main_app.models import CustomUser, Course, Student, Session
from django.core.management import call_command
import uuid

class CustomUserModelTest(TestCase):
	def setUp(self):
		self.user = CustomUser.objects.create_user(email='test@example.com', password='testpass123', user_type=1)
      
	def test_user_creation(self):
		"""Test that a CustomUser is created with the correct email and user_type."""
		self.assertEqual(self.user.email, 'test@example.com')
		self.assertEqual(self.user.user_type, 1)
		self.assertTrue(self.user.check_password('testpass123'))

	def test_str_method(self):
		self.user.save()
		self.assertEqual(str(self.user), 'test@example.com')
  


class CourseModelTest(TestCase):
	def test_course_str(self):
		course = Course.objects.create(name='Mathematics')
		self.assertEqual(str(course), 'Mathematics')

class StudentModelTest(TestCase):
	def setUp(self):
		# Use a unique email for each test run to avoid unique constraint issues
		unique_email = f"student_{uuid.uuid4().hex}@example.com"
		self.user = CustomUser.objects.create_user(email=unique_email, password='pass', user_type=3)
		self.session = Session.objects.create(start_year='2022-01-01', end_year='2023-01-01')
		self.course = Course.objects.create(name='Physics')
		# get_or_create returns (obj, created) - unpack to get the instance
		self.student, _created = Student.objects.get_or_create(
			student=self.user,
			defaults={'course': self.course, 'session': self.session}
		)

	def test_student_str(self):
		# Student.__str__ should include the related user's email (adjust if model returns full name)
		self.assertEqual(str(self.student), self.user.email)
