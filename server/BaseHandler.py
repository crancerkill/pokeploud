import webapp2

from webapp2_extras import sessions

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session(max_age=30)

    def setSessionParameter(self, key, value):
        """
        Set a parameter in user session
        @param key: the parameter name
        @param value: the parameter value
        """
        self.session[key] = value

    def getSessionUser(self):
        """
        Return the connected user from the session
        :return: the user dict
        """
        return self.session.get('user', {})