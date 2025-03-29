from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.company import views as company_views

router=DefaultRouter()
router.register(r'companies', company_views.CompanyViewSet, basename='company-view-set')

urlpatterns=[
    path('',include(router.urls)),
]