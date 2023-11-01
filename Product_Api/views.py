# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import viewsets,filters
# from .models import Product
# from .serializers import Product_serializers
# from rest_framework.pagination import PageNumberPagination
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from django.db.models import Q 
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.settings import api_settings
# from rest_framework import permissions

# from django_filters import rest_framework as filters
# from rest_framework import viewsets
# from .models import Product
# from .serializers import Product_serializers
# from rest_framework import permissions

# class ProductFilter(filters.FilterSet):
#     search = filters.CharFilter(method='custom_search')

#     class Meta:
#         model = Product
#         fields = []

#     def custom_search(self, queryset, name, value):
#         return queryset.filter(Q(name__icontains=value) | Q(category__product_category__icontains=value))

# class ProductViewsets(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = Product_serializers
#     filter_backends = [filters.DjangoFilterBackend]  # Use DjangoFilterBackend
#     filterset_class = ProductFilter  # Use the custom filter class
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]




# # class ProductViewsets(viewsets.ModelViewSet):
# #     queryset=Product.objects.all()
# #     serializer_class=Product_serializers
# #     filter_backends=[filters.SearchFilter]
# #     search_fields=['name']
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     # pagination_class = PageNumberPagination()  # Add this line




# # Import the User model

# class UserRegistrationView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not username or not email or not password:
#             return Response({'message': 'Username, email, and password are required'}, status=status.HTTP_400_BAD_REQUEST)

#         # Check if a user with the provided username or email already exists
#         if User.objects.filter(Q(username=username) | Q(email=email)).exists():
#             return Response({'message': 'Username or email already exists'}, status=status.HTTP_400_BAD_REQUEST)

#         # If the user does not exist, create a new user
#         user = User.objects.create_user(username=username, email=email, password=password)
#         refresh=RefreshToken.for_user(user)
#         print(refresh)
#         accessToken = str(refresh.access_token)
#         print("accessToken -------- ", accessToken)
#         return Response({
#             'message': 'User registered successfully',
#             'access_token': str(refresh.access_token),
#             'refresh_token': str(refresh)
#         }, status=status.HTTP_201_CREATED)

# class UserLoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         if not username or not password:
#             return Response({'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             # Generate a JWT token for the user
#             refresh = RefreshToken.for_user(user)

#             # Get the token data
#             token_data = {
#                 'access_token': str(refresh.access_token),
#                 'refresh_token': str(refresh),
#             }

#             return Response({
#                 'message': 'User logged in successfully',
#                 **token_data
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from .models import Product
from .serializers import Product_serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.settings import api_settings
from rest_framework import permissions
from django_filters import rest_framework as filters

# Import User model
from rest_framework import viewsets

# Import the Product model and serializer
from .models import Product
from .serializers import Product_serializers

# Import permissions module
from rest_framework import permissions

# Define a custom filter for the Product model
class ProductFilter(filters.FilterSet):
    search = filters.CharFilter(method='custom_search')

    class Meta:
        model = Product
        fields = []

    def custom_search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(category__product_category__icontains=value))

# Define a viewset for the Product model
class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_serializers
    filter_backends = [filters.DjangoFilterBackend]  # Use DjangoFilterBackend
    filterset_class = ProductFilter  # Use the custom filter class
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Define a view for user registration
class UserRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'message': 'Username, email, and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if a user with the provided username or email already exists
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return Response({'message': 'Username or email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # If the user does not exist, create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        refresh = RefreshToken.for_user(user)
        accessToken = str(refresh.access_token)

        return Response({
            'message': 'User registered successfully',
            'access_token': accessToken,
            'refresh_token': str(refresh)
        }, status=status.HTTP_201_CREATED)

# Define a view for user login
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate a JWT token for the user
            refresh = RefreshToken.for_user(user)

            # Get the token data
            token_data = {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }

            return Response({
                'message': 'User logged in successfully',
                **token_data
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

from rest_framework.generics import GenericAPIView
class API(GenericAPIView):
    serializer_class=Product_serializers