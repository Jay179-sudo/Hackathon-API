# urls.py


from .views import HackathonView, UserEnrolledHackathonsListView, UserSubmissionsListView, HackathonDetailView, UserEnrolledHackathonsDetailView, UserSubmissionDeleteView
from django.urls import path
urlpatterns = [
    path('hackathons/', HackathonView.as_view(), name='hackathon'),
    path('hackathons/user/', UserEnrolledHackathonsListView.as_view(), name='user_list'),
    path('hackathons/user/submissions/', UserSubmissionsListView.as_view(), name='user_submit_list'),

    path('hackathons/<str:pk>', HackathonDetailView.as_view(), name='hackathon_del'),
    path('hackathons/user/<str:pk>/', UserEnrolledHackathonsDetailView.as_view(), name='user_hackathon_detail'),
    path('hackathons/user/submissions/<str:pk>/', UserSubmissionDeleteView.as_view(), name='user_hackathon_delete'),
]
