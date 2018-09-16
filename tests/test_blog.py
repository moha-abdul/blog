import unittest
from app.models import User, Blog
from flask_login import current_user
from app import db

class TestBlog(unittest.TestCase):

    def setUp(self):
        self.user_Melissa = User(username = 'maxa',password = 'awesome',email = 'awesome@awe.com')
        self.new_blog = Blog(id = 90,title = 'New Blog', content = "blah blah blah", comments = "love your blog",user_id = self.user_maxa)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,90)
        self.assertEquals(self.new_blog.title,'New Blog')
        self.assertEquals(self.new_blog.content,"blah blah blah")
        self.assertEquals(self.new_blog.comments, 'love your blog')
        self.assertEquals(self.new_blog.user,self.user_maxa)
