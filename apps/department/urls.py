from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.department import views as department_views

router=DefaultRouter()
router.register(r'departments', department_views.DepartmentViewSet, basename='department-view-set')

urlpatterns=[
    path('',include(router.urls)),
]