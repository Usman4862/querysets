from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

class FakeRateThrottle(generics.ListCreateAPIView):
    queryset = FakeThrottle.objects.all()
    serializer_class = FakeThrottleSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class SingleRateThrottle(generics.RetrieveUpdateDestroyAPIView):
    queryset = FakeThrottle.objects.all()
    serializer_class = FakeThrottleSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    lookup_field = 'id'

