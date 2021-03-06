# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import SongSerializer, ImageSerializer, StorySerializer, FeedbackSerializer, Music_Video_Serializer, Poem_Serializer, CustomUserSerializer
from .models import Song, Image, Story, Feedback, Music_Video, Poem, Custom_User
from rest_framework.documentation import include_docs_urls
from . import models
from . import serializers
from django.contrib.auth import hashers


def index(request):
    return HttpResponse("Models API")

class SongCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class SongDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    # def delete(self, request, pk, format=None):
    #     song = Song.objects.get(pk=pk)
    #     song.delete()

class SongListView(generics.ListCreateAPIView):
    """This class handles the http GET and PUT requests for multiple instances of a song."""
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ImageCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class ImageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    # def delete(self, request, pk, format=None):
    #     image = Image.objects.get(pk=pk)
    #     image.delete()

class ImageListView(generics.ListCreateAPIView):
    """This class handles the http GET and PUT requests for multiple instances of an image."""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class Music_Video_CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Music_Video.objects.all()
    serializer_class = Music_Video_Serializer

    def perform_create(self, serializer):
    	serializer.save()

class Music_Video_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Music_Video.objects.all()
    serializer_class = Music_Video_Serializer

    # def delete(self, request, pk, format=None):
    #     vid = Music_Video.objects.get(pk=pk)
    #     vid.delete()

class Music_Video_ListView(generics.ListCreateAPIView):
    """This class handles the http GET and PUT requests for multiple instances of a music video."""
    queryset = Music_Video.objects.all()
    serializer_class = Music_Video_Serializer

class Poem_CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Poem.objects.all()
    serializer_class = Poem_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class Poem_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Poem.objects.all()
    serializer_class = Poem_Serializer

    # def delete(self, request, pk, format=None):
    #     poem = Poem.objects.get(pk=pk)
    #     poem.delete()

class Poem_ListView(generics.ListCreateAPIView):
    """This class handles the http GET and PUT requests for multiple instances of a poem."""
    queryset = Poem.objects.all()
    serializer_class = Poem_Serializer

class StoryCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class StoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    # def delete(self, request, pk, format=None):
    #     story = Story.objects.get(pk=pk)
    #     story.delete()

class Story_ListView(generics.ListCreateAPIView):
    """This class handles the http GET and PUT requests for multiple instances of a story."""
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class FeedbackCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class FeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    # def delete(self, request, pk, format=None):
    #     feedback = Feedback.objects.get(pk=pk)
    #     feedback.delete()

class CustomUserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Custom_User.objects.all()
    serializer_class = CustomUserSerializer

    # def delete(self, request, pk, format=None):
    #     user = Custom_User.objects.get(pk=pk)
    #     user.delete()

class CustomUserListCreateView(generics.ListCreateAPIView):
    """This class handles the http GET and PUT requests for multiple instances of a user."""
    queryset = Custom_User.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned user to a given username,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Custom_User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

class AuthCreateView(generics.CreateAPIView):
    """Handles POST requests for authenticators"""
    queryset = models.Authenticator.objects.all()
    serializer_class = serializers.AuthenticatorSerializer

class AuthRetrieveView(generics.RetrieveAPIView):
    """Handles GET requests for a single authenticator identified by its user_id"""
    queryset = models.Authenticator.objects.all()
    serializer_class = serializers.AuthenticatorSerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user_id = self.kwargs['user_id']
        return models.Authenticator.objects.filter(user_id=user_id)

class AuthDestroyView(generics.DestroyAPIView):
    """Handles DELETE requests for a single authenticator identified by its pk (the authenticator value)"""
    queryset = models.Authenticator.objects.all()
    serializer_class = serializers.AuthenticatorSerializer

class SparkEntryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Spark_Entries.objects.all()
    serializer_class = serializers.SparkEntrySerializer