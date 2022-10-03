from django.urls import path
from sa_page.views import *


urlpatterns = [
    path('', index, name='index'),
    path('pd_data/', usage, name='pd_data'),
    path('voting/', voting, name='voting'),
    path('events/', events, name='events'),
    path('ssotest/', ssotest, name='ssotest'),
    path('functionintro/', businesscard, name='functionintro'),
    path('functionintro/businesscard/', businesscard, name='businesscard'),
    path('functionintro/community/', community, name='community'),
    path('functionintro/sellingprocess/', sellingprocess, name='sellingprocess'),
    path('functionintro/customertagfilter/', customertagfilter, name='customertagfilter'),
    path('functionintro/productcart/', productcart, name='productcart'),
]
