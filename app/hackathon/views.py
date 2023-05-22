# views.py

from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Hackathon, Submission, Enrollment
from .serializers import HackathonSerializer, UserEnrolledHackathonsSerializer, UserSubmissionsSerializer, HackathonDeleteSerializer, UserEnrolledHackathonDetailSerializer

class HackathonView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class HackathonDetailView(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Hackathon.objects.all()
    serializer_class = HackathonDeleteSerializer

    def get_queryset(self):
        name = self.kwargs.get('pk')
        user = self.request.user
        queryset = Hackathon.objects.filter(created_by=user, title=name)
        return queryset


class UserEnrolledHackathonsListView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserEnrolledHackathonsSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Enrollment.objects.filter(user=user)
        return queryset
    
class UserEnrolledHackathonsDetailView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserEnrolledHackathonDetailSerializer

    def get_queryset(self):
        user = self.request.user
        enrollment_id = self.kwargs.get('pk')
        hello = Hackathon.objects.filter(title=enrollment_id)
        queryset = Enrollment.objects.filter(hackathon__in=hello, user=user)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        return obj
    def perform_destroy(self, instance):
        user = self.request.user
        submissions = Submission.objects.filter(user=user, hackathon=instance.hackathon)
        submissions.delete()
        instance.delete()



class UserSubmissionsListView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSubmissionsSerializer

    def get_queryset(self):
        user = self.request.user
        return Submission.objects.filter(user=user)
    
class UserSubmissionDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSubmissionsSerializer
    queryset = Submission.objects.all()

    def get_object(self):
        user = self.request.user
        submission_id = self.kwargs.get('pk')
        queryset = self.get_queryset().filter(name=submission_id, user=user)
        obj = generics.get_object_or_404(queryset)
        return obj

    def perform_destroy(self, instance):
        instance.delete()