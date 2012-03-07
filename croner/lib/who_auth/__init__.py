from pylons import url
from pylons.controllers.util import redirect
from pylons import session, request, response


class WhoAuthPlugin(object):
    def authenticate(self, environ, identity):
        return identity['login']


class WhoIdentPlugin(object):
    def identify(self, environ):
        beaker = environ.get('beaker.session')

        if not beaker or not 'logged_user' in beaker:
            return None

        return beaker['logged_user']

    def remember(self, environ, identity):
        beaker = environ.get('beaker.session')

        beaker['logged_user'] = identity
        beaker.save()

    def forget(self, environ, identity):
        beaker = environ.get('beaker.session')

        if 'logged_user' in beaker:
            del beaker['logged_user']

        beaker.save()
