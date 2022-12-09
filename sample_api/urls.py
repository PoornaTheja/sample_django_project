from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('products/', views.product_home_view, name="product_home"),
    path('product/<str:prod_name>/', views.product_sep_view, name="product_sep")
]