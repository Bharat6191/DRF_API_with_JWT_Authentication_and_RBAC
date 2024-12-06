from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer,ProjectSerializer
from .models import Project

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({"access_token": str(refresh.access_token)}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        project=Project.objects.all()
        serializer=ProjectSerializer(project,many=True)
        return Response({"projects": serializer.data},status=200)

class AdminProjectView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print(request.user.role)
        if request.user.role== 'admin':
            data=request.data.copy()
            data['created_by']=request.user.id
            serializer=ProjectSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Project created successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Bad Data."},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token or token already blacklisted."}, status=status.HTTP_400_BAD_REQUEST)
