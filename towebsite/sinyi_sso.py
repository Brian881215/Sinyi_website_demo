from django.urls import path
from django.shortcuts import render, redirect
from django.urls import reverse
from functools import wraps
from uuid import uuid4
import requests


# show profile structure


class SinyiSSO:
    def __init__(self, client_id, client_secret, redirect_domain,
                        auth_server_uri, recource_server_uri,
                        unauth_path, signin_page):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_server_uri = auth_server_uri
        self.recource_server_uri = recource_server_uri
        self.unauth_path = unauth_path
        self.signin_page = signin_page

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
            'unauth': 'Visiting this page requires you to be <strong>authenticated</strong>.',
        }

        # redirect_domain = ex: http://localhost:8000/auth, https://to.sinyi.com.tw/auth
        redirect = self.url_path['redirect']
        self.redirect_uri = f'{redirect_domain}/{redirect}'

    def url_patterns(self):
        return [
            path(self.url_path['sign_in'], self.sign_in, name='sign_in'),
            path(self.url_path['redirect'], self.redirect, name='redirect'),
        ]

    def get_auth_uri(self, request):
        # debug
        print('get_auth_uri')

        state = str(uuid4())
        request.session['user_state'] = state
        client = self.auth_server_params['client_id']
        redirect = self.auth_server_params['redirect_uri']

        # encode
        return f'{self.auth_server_uri}?state={state}&{client}={self.client_id}&{redirect}={self.redirect_uri}'

    def check_state(self, request):
        return_state = request.GET.get('state', '')
        session_state = request.session.get('state', None)

        # debug
        print('check_state')
        print('return_state', return_state)
        print('session_state', session_state)

        if session_state is None or session_state != return_state:
            return render(request,
                            self.unauth_path,
                            {'message': self.auth_error_message['state_error']})

    def get_user_profile(self, request):
        # debug
        print('get_user_profile')

        sinyi_resource_server = self.recource_server_uri
        auth_code = request.GET.get(self.resorce_server_params['auth_code'], '')
        body = {
            self.resource_server_params['client_id']: self.client_id,
            self.resource.server_params['client_secret']: self.client_secret,
            self.resource.server_params['auth_code']: auth_code,
        }
        user_profile = requests.post(sinyi_resource_server, json=body).json()

        if user_profile: # how to check
            request.session['user_profile'] = user_profile
            request.session['is_auth'] = True

            # debug
            print('profile', request.session['user_profile'])
            print('is_auth', request.session['is_auth'])
        else:
            return render(request,
                            self.unauth_path,
                            {'massage': self.auth_error_message['get_profile_error']})

    def sign_in(self, request):
        # debug
        print('sign_in')

        auth_uri = self.get_auth_uri(request)

        # debug
        print(auth_uri)

        return redirect(auth_uri)

    def redirect(self, request):
        # debug
        print('redirect')

        # check if this auth was processed by server
        self.check_state(request)

        # get user profile and save to session
        # sinyi sso does not have single sign out, you can set the deadline of session by yourself
        self.get_user_profile(request)

        return redirect(reverse(self.signin_page))

    def login_required(self, f):
        @wraps(f)
        def assert_login(*args, **kwargs):
            # debug
            print('login_required')
            print('is_auth', args[0].session.get('is_auth', False))
            print('user_profile', args[0].session.get('user_profile'))

            if not args[0].session.get('is_auth', False):
                # debug
                print('is_auth = False')

                return redirect(reverse('sign_in'))

            # debug
            print('is_auth = True')

            return f(*args, **kwargs)
        return assert_login
