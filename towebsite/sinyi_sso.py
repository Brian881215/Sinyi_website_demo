from django.urls import path
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from functools import wraps
from uuid import uuid4
import requests
from urllib.parse import quote
import logging
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SinyiSSO:
    def __init__(self, client_id, client_secret, redirect_domain,
                        auth_server_uri, recource_server_uri):
        log_dir = os.path.join(BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        logging.basicConfig(filename=log_dir+'/sinyi_sso.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S', level=logging.DEBUG)
        self.logger = logging.getLogger()

        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_server_uri = auth_server_uri
        self.recource_server_uri = recource_server_uri

        self.auth_server_params = {
            'client_id': 'ClientId',
            'redirect_uri': 'redirectUri',
        }
        self.resource_server_params = {
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'auth_code': 'authCode',
        }
        self.url_path = {
            'sign_in': 'sign_in',
            'redirect': 'redirect',
        }
        self.auth_error_message = {
            'state_error': 'Failed to match request state with session state.',
            'get_profile_error': 'Failed to get the user profile from sinyi resource server, please contact tech support.',
        }

        # redirect_domain = ex: http://localhost:8000/auth, https://to.sinyi.com.tw/auth
        redirect = self.url_path['redirect']
        self.redirect_uri = quote(f'{redirect_domain}/{redirect}', safe='')

    def url_patterns(self):
        return [
            path(self.url_path['sign_in'], self.sign_in, name='sign_in'),
            path(self.url_path['redirect'], self.redirect, name='redirect'),
        ]

    def get_auth_uri(self, request):
        state = str(uuid4())
        request.session['user_state'] = state
        client = self.auth_server_params['client_id']
        redirect = self.auth_server_params['redirect_uri']

        return f'{self.auth_server_uri}?{client}={self.client_id}&{redirect}={self.redirect_uri}?state={state}'

    def check_state(self, request):
        return_state = request.GET.get('state', '')
        session_state = request.session.get('user_state', None)

        if session_state is None or session_state != return_state:
            self.logger.error(self.auth_error_message['state_error'])
            return HttpResponse(self.auth_error_message['state_error']+
                                '<br/><a href="/auth/sign_in">Retry</a>',
                                status=401)

        return True

    def get_user_profile(self, request):
        sinyi_resource_server = self.recource_server_uri
        auth_code = request.GET.get(self.resource_server_params['auth_code'], '')
        body = {
            self.resource_server_params['client_id']: self.client_id,
            self.resource_server_params['client_secret']: self.client_secret,
            self.resource_server_params['auth_code']: auth_code,
        }
        response = requests.post(sinyi_resource_server, json=body)
        if response.status_code != 200:
            self.logger.error('Unable to get user profile: '+response.text)
            return HttpResponse(response.text,
                                status=response.status_code)
        user_profile = response.json()

        if user_profile['state'] != 200:
            self.logger.error(self.auth_error_message['get_profile_error'])
            return HttpResponse(self.auth_error_message['get_profile_error']+
                                '<br/>'+str(user_profile['ErrDesc'])+
                                '<br/><a href="/auth/sign_in">Retry</a>',
                                status=401)
        request.session['user_profile'] = user_profile
        request.session['is_auth'] = True

        return True

    def sign_in(self, request):
        auth_uri = self.get_auth_uri(request)

        return redirect(auth_uri)

    def redirect(self, request):
        # check if this auth was processed by server
        check_state = self.check_state(request)
        if check_state != True:
            return check_state

        # get user profile and save to session
        # sinyi sso does not have single sign out, you can set the deadline of session by yourself
        get_user_profile = self.get_user_profile(request)
        if get_user_profile != True:
            return get_user_profile

        redirect_after_signin = request.session.get('redirect_after_signin', False)
        if not redirect_after_signin:
            self.logger.error('Could not get the redirect url after signing in.')
            return HttpResponse('Could not get the redirect url after signing in.',
                                status=500)
        return redirect(redirect_after_signin)

    def login_required(self, f):
        @wraps(f)
        def assert_login(*args, **kwargs):
            if not args[0].session.get('is_auth', False):
                self.logger.error('Unauthorized... Redirecting to sign_in page.')
                args[0].session['redirect_after_signin'] = args[0].get_full_path_info()
                return redirect(reverse('sign_in'))
            return f(*args, **kwargs)

        return assert_login
