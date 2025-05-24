from rest_framework import serializers
from .models import Member, MemberDetails
from django.contrib.auth.models import User

from AirArctic import settings



class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member

        fields = ['memberId', 'firstName', 'lastName', 'contactNumber', 'emailAddress', 'dateRegistered','rewardsLevel','totalPoints']


class LoginSerializer(serializers.Serializer):
        
     username = serializers.CharField()
     password = serializers.CharField()

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name')

class MemberDetailsSerializer(serializers.HyperlinkedModelSerializer):

   user = CurrentUserSerializer(read_only=True)
   user_id = serializers.IntegerField(write_only = True)
   

   class Meta:
        model = MemberDetails

        
        fields = ['id', 'user', 'user_id', 'contactNumber', 'emailAddress','rewardsLevel','totalPoints']





'''
class LoyaltySerializer(serializers.ModelSerializer):


    memberDetail = MemberSerializer(read_only=True)

    class Meta:
        model = LoyaltyProgram
        fields = ['id', 'memberDetail', 'rewardsLevel', 'totalPoints']
        
'''
