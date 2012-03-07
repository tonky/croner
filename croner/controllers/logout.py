import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from croner.lib.base import BaseController, render
from repoze.who.api import get_api

log = logging.getLogger(__name__)

class LogoutController(BaseController):
    def index(self):
        # who_api = get_api(request.environ)

        # print who_api

        # print who_api.forget()

        abort(401)
        # redirect(url(controller='login'))
