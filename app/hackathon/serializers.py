# serializers.py

from rest_framework import serializers
from .models import Hackathon, Submission, Enrollment
from django.core.exceptions import ObjectDoesNotExist


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ('title', 'description', 'background_image', 'hackathon_image', 'type_of_submission', 'start_datetime', 'end_datetime', 'reward_prize')
    def save(self, **kwargs):

        request = self.context.get('request',  None)
        if request:
            kwargs["created_by"] = request.user
            return super().save(**kwargs)

class HackathonDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ('title', 'description', 'background_image', 'hackathon_image', 'type_of_submission', 'start_datetime', 'end_datetime', 'reward_prize')

class UserEnrolledHackathonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = ('user', 'hackathon',)
class UserEnrolledHackathonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = ('hackathon', )

    def create(self, validated_data):
        hackathon = validated_data.pop('hackathon')
        user = self.context['request'].user

        enrollment = Enrollment.objects.create(hackathon=hackathon, user=user)
        return enrollment

class UserSubmissionsSerializer(serializers.ModelSerializer):
    hackathon = serializers.PrimaryKeyRelatedField(queryset=Hackathon.objects.all())

    class Meta:
        model = Submission
        fields = ('hackathon', 'name', 'summary', 'submission_file', 'submission_link')

    def validate(self, attrs):
        type_of_submission = attrs.get('hackathon').type_of_submission
        print(type_of_submission == 'link')
        print(attrs['submission_file'] == None)

        if attrs['submission_file'] == None and attrs['submission_link'] == '':
            raise serializers.ValidationError("Invalid submission type. File or link expected")
        if attrs['submission_file'] != None and attrs['submission_link'] != '':
            raise serializers.ValidationError("Invalid submission type. Both file and link not expected")
    
        
        if type_of_submission == 'image' or type_of_submission == 'file':
            if attrs['submission_file'] == None and attrs['submission_link'] != '':
                raise serializers.ValidationError("Invalid submission type. File expected")
            else:
                return attrs
        elif type_of_submission == 'link':
            if attrs['submission_link'] == '' and attrs['submission_file'] != None:
                raise serializers.ValidationError("Invalid submission type. Link Expected")
            else:
                return attrs
        

    
    def create(self, validated_data):
        hackathon = validated_data.pop('hackathon')
        user = self.context['request'].user

        enrollments = Enrollment.objects.filter(user=user)
        for enrolled in enrollments:
            userHack=enrolled.hackathon

            if(hackathon == userHack):
                hackathon_instance = hackathon
        

                submission = Submission.objects.create(hackathon=hackathon_instance, user=user, **validated_data)
                return submission

        raise serializers.ValidationError("User has not participated in this hackathon")
   