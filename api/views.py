
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.throttling import JackRateThrottle


class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_classes=[SessionAuthentication]
	permission_classes=[IsAuthenticatedOrReadOnly]
	throttle_classes=[AnonRateThrottle,JackRateThrottle]