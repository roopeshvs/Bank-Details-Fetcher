from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers, viewsets

from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailView, ListView
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register('banks',views.BankView)
router.register('branchlist',views.BranchesView)

urlpatterns = [
    path('',include(router.urls)),
    url(r'^ifsc/(?P<ifsc>[A-Za-z]{4}\w{7})$', DetailView.as_view()),
    url(r'^branches/(?P<city>.*)/(?P<bank>.*)$', ListView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]