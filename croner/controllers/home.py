import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from croner.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HomeController(BaseController):
    def index(self):
        print session

        if not 'user' in session:
            redirect(url(controller='login'))

        # Return a rendered template
        return render('/index.mako', {'name': session['user']})
