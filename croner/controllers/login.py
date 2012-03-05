import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from croner.lib.base import BaseController, render, Session
from croner.model import User

log = logging.getLogger(__name__)

class LoginController(BaseController):
    def index(self):
        return render('/login.mako')

    def save(self):
        login = request.params['login']
        password = request.params['password']

        user = Session.query(User).filter_by(login=login, passwd=password).first()

        if not user:
            return render('/login.mako', {'error': 'wrong credentials'})

        session['user'] = user.name
        session.save()

        redirect(url(controller='home'))
