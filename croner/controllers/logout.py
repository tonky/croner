import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from croner.lib.base import BaseController, render

log = logging.getLogger(__name__)

class LogoutController(BaseController):
    def index(self):
        del session['user']
        session.save()

        redirect(url(controller='login'))
