# Configuration file for jupyterhub.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#c.Application.log_level = 30

#------------------------------------------------------------------------------
# JupyterHub(Application) configuration
#------------------------------------------------------------------------------

## An Application for starting a Multi-User Jupyter Notebook server.

## Maximum number of concurrent servers that can be active at a time.
#  
#  Setting this can limit the total resources your users can consume.
#  
#  An active server is any server that's not fully stopped. It is considered
#  active from the time it has been requested until the time that it has
#  completely stopped.
#  
#  If this many user servers are active, users will not be able to launch new
#  servers until a server is shutdown. Spawn requests will be rejected with a 429
#  error asking them to try again.
#  
#  If set to 0, no limit is enforced.
#c.JupyterHub.active_server_limit = 0

## Duration (in seconds) to determine the number of active users.
#c.JupyterHub.active_user_window = 1800

## Grant admin users permission to access single-user servers.
#  
#  Users should be properly informed if this is enabled.
#c.JupyterHub.admin_access = False

## Class for authenticating users.
#  
#          This should be a subclass of :class:`jupyterhub.auth.Authenticator`
#  
#          with an :meth:`authenticate` method that:
#  
#          - is a coroutine (asyncio or tornado)
#          - returns username on success, None on failure
#          - takes two arguments: (handler, data),
#            where `handler` is the calling web.RequestHandler,
#            and `data` is the POST form data from the login page.
#  
#          .. versionchanged:: 1.0
#              authenticators may be registered via entry points,
#              e.g. `c.JupyterHub.authenticator_class = 'jwtauthenticator.jwtauthenticator.JSONWebTokenLocalAuthenticator'
#  
#  Currently installed: 
#    - default: jupyterhub.auth.PAMAuthenticator
#    - dummy: jupyterhub.auth.DummyAuthenticator
#    - pam: jupyterhub.auth.PAMAuthenticator

# c.Authenticator.delete_invalid_users = True
# c.Authenticator.username_map = {'usithornbe': 'tobias'}

# c.Authenticator.admin_users = {"tobias"}
c.JupyterHub.authenticator_class = 'jwtauthenticator.jwtauthenticator.JSONWebTokenLocalAuthenticator'
# c.LocalAuthenticator.create_system_users=True
# c.JSONWebTokenAuthenticator.delete_invalid_users = True


# # added configuration for jwt auth
from urllib import request
secretUrl = 'https://keycloak4dev.usu-research.ml/auth/realms/mandant1/protocol/openid-connect/certs'
with request.urlopen(secretUrl) as response:
    c.JSONWebTokenAuthenticator.secret = response.read().decode()
c.JSONWebTokenAuthenticator.username_claim_field = 'preferred_username'
c.JSONWebTokenAuthenticator.expected_audience = ''    
c.JSONWebTokenAuthenticator.param_name = 'token'
# c.JSONWebLocalTokenAuthenticator.create_system_users = True 

