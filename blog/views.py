import uuid
from blog.utils.drf import BlogViewSet
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import UserSerializer
from blog.utils.django import get_or_none


class UserAccountViewSet(BlogViewSet):
    def check_permissions(self, request):
        pass

    def authenticate(self, request):
        
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return self.error_response(status=HTTP_400_BAD_REQUEST, msg = "", data={"errors":serializer.errors})

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(username = email, password=password)

        if user is None:
            return self.error_response(status = HTTP_400_BAD_REQUEST, msg = "", data = {"errors":"Invalid creadentails"})

        return self.success_response(status = HTTP_200_OK, msg  = "", data = {})  

    def create_user(self, request):

        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return self.error_response(status=HTTP_400_BAD_REQUEST, msg = "", data={"errors":serializer.errors})

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = get_or_none(User, username = email)

        if user:
            self.error_response(status = HTTP_400_BAD_REQUEST, msg = "", data = {"error": "Username already exists"})

        User.objects.create_user(username = email, password = password)

        return self.success_response(status=HTTP_200_OK, msg = "", data = {})

    def change_password(self, request):


        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return self.error_response(status=HTTP_400_BAD_REQUEST, msg = "", data={"errors":serializer.errors})

        email = serializer.validated_data["email"]

        new_password = serializer.validated_data["password"]

        user = get_or_none(User, username = email)

        if user is None:
            return self.error_response(status=HTTP_400_BAD_REQUEST, msg = "", data= {"error": "No user found with this email"})
        
        user.set_password(new_password)
        user.save()

        return self.success_response(status = HTTP_200_OK, msg = "", data = {} )



        
        

        
        
        
    
            

        

        


            
                
   
        

        

        
