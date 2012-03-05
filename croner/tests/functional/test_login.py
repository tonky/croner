from croner.tests import *
from nose.tools import ok_, eq_
from urlparse import urlparse
from webtest import TestApp


class TestLoginController(TestController):
    def setUp(self):
        self.app = TestApp("config:test.ini", relative_to="/Users/tonky/projects/Croner")

    def tearDown(self):
        pass

    def test_login_index(self):
        response = self.app.get(url(controller='login'))
        ok_('Login' in response.body)

    def test_bad_password(self):
        response = self.app.request("/login/save", POST={'login': 'joe', 'password': '2'})

        ok_('wrong' in response.body)

    def test_do_login(self):
        response = self.app.request("/login/save", POST={'login': 'joe', 'password': '1'})

        eq_(response.status, "302 Found")
        home = response.follow()
        ok_('Welcome, Joe!' in home.body)
