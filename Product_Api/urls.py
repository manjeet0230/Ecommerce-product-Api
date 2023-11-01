
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Product_Api.views import ProductViewsets
from .views import UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView,TokenVerifyView ) 



router=DefaultRouter()
router.register('product',ProductViewsets,basename='Product')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/login/', UserLoginView.as_view(), name='user_login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

                