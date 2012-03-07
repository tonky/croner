import logging
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from repoze.who.api import get_api

from croner.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HomeController(BaseController):
    def index(self):
        who_api = get_api(request.environ)

        user = who_api.authenticate()

        if not user:
            return who_api.challenge()

        # Return a rendered template
        return render('/index.mako', {'user': user})
