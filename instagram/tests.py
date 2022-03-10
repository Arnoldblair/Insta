from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image,Like,Comment,Profile

# Create your tests here.
class CommentTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(user='blair',password='admin123')
        self.comment = Comment(comment='Test Comment',user=self.new_user,post=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def tearDown(self):
        Comment.objects.all().delete()

    def test_save_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)

class ImageTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user.objects.create_user('blair')
        cls.new_profile = Profile (profile_pic='')    
        cls.new_image = Image(my_image='', caption='hello', profile=cls.new_profile)

    def test_instance_true(cls):
        cls.assertTrue(isinstance(cls.new_image, Image))

    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()              

class Intagram_TestCases(TestCase):
    def setUp(self):
        self.user1= User(id=1,username='blair',email='arnoldblair.munene@student.moringaschool.com',password='12244')
        self.user1.save()
        self.profile = Profile(user_id=1,bio='hello world',profile_pic='')
        self.profile.save_profile()
        self.my_image = Image(id=1,caption='my first program', owner=self.user1,profile=self.profile,image='',image_name='python')
        self.my_image.save_image()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.my_image,Image))

    def test_save_method(self):
        self.my_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.my_image.save_image()
        object = Image.objects.filter(id=1)
        Image.delete_image(object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)


    def test_get_image_by_id(self):
        self.my_image.save_image()
        image = Image.get_image_by_id(1)
        self.assertEqual(image.id,1)


    def test_update_single_image(self):
        self.my_image.save_image()
        filtered_object =Image.update_image('python','prog')
        updated = Image.objects.get(image_name='prog')
        self.assertEqual(updated.image_name,'prog')