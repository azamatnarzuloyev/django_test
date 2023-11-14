from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from  rest_framework.decorators import APIView
from .serializers import AuthenticationSerializer, AUthouserSerializer, UsersListSerializer, UserProfileSerializer, CreateTwoStepPasswordSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class Register(APIView):
    """
    post:
        Send mobile number for Register.
        parameters: [phone,]
    """

    # throttle_scope = "authentication"
    # throttle_classes = [
    #     ScopedRateThrottle,
    # ]
    def post(self, request):
        serializer = AUthouserSerializer(data=request.data)
        if serializer.is_valid():
            received_phone = serializer.data.get("phone")
            shop_password = serializer.data.get("shop_password")
 
            user_is_exists: bool = get_user_model().objects.filter(phone=received_phone).values("phone").exists()
            if user_is_exists:
                return Response(
                    {
                        "User exists.": "Please enter a different phone number.",
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            # The otp code is sent to the user's phone number for authentication
            else:
                user, created = get_user_model().objects.get_or_create(phone=received_phone, shop_password=shop_password)
                refresh = RefreshToken.for_user(user)
                
                context = {
                        "created": created,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                return Response(context, status=status.HTTP_201_CREATED)

        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST,               
            )
        

class UsersList(ListAPIView):
    """
    get:
        Returns a list of all existing users.
    """

    serializer_class = UsersListSerializer
    # permission_classes = [
    #     permissions.IsAdminUser,
    # ]
    filterset_fields = [
        # "author",
        'phone',
    ]
    # search_fields = [
    #     "phone",
    #     "first_name",
    #     "last_name",
    # ]
    # ordering_fields = (
    #     "id", "author",
    # )

    def get_queryset(self):
        return get_user_model().objects.all()
    
class UserProfile(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the profile of user.
    put:
        Update the detail of a user instance
        parameters: exclude[password,]
    delete:
        Delete user account.
        
        parameters: [pk]
    """

    serializer_class = UserProfileSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user
    


class Login(APIView):
    """
    post:
        Send mobile number for Login.
        parameters: [phone,]
    """

  

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            received_phone = serializer.data.get("phone")
            shop_password = serializer.data.get("shop_password")

            user_is_exists: bool = get_user_model().objects.filter(phone=received_phone).values("phone").exists()
            if not user_is_exists:
                return Response(
                    {
                        "No User exists.": "Please enter another phone number.",
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            # The otp code is sent to the user's phone number for authentication
            else:
                user, created = get_user_model().objects.get_or_create(phone=received_phone, shop_password=shop_password)
                refresh = RefreshToken.for_user(user)
                
                context = {
                        "created": created,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                return Response(context, status=status.HTTP_201_CREATED)


        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST,
            )
        


