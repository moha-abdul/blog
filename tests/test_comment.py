import unittest
from app.models import Comment,User
from flask_login import current_user
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_maxa = User(username = 'maxa',password = 'awesome',email = 'awesome@awe.com')
        self.new_comment = Comment(id = 90,post_comment = "great blog", blogs = "hello blog world", user_id = self.user_maxa)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,12345)
        self.assertEquals(self.new_comment.post_comment,"great blog")
        self.assertEquals(self.new_comment.blog, 'hello blog world')
        self.assertEquals(self.new_comment.user,self.user_maxa)
