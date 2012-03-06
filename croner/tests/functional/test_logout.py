from croner.tests import *
from nose.tools import ok_, eq_
from pylons import request, response, session, tmpl_context as c, url

class TestLogoutController(TestController):
    def test_logout(self):
        response = self.app.post("/login/save", {'login': 'joe', 'password': '1'})
        home = response.follow()
        ok_('Welcome, Joe!' in home.body)

        response = self.app.post("/logout")
        login = response.follow()
        print login
        ok_('Login' in login.body)
