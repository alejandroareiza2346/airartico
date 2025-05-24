from django.shortcuts import render
from django.db import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Member, MemberDetails
from .serializers import MemberSerializer, LoginSerializer, MemberDetailsSerializer
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate

#========
# API Implementation 
#========

class LoginAPI(APIView):
     def post(self, request):
          data = request.data
          serializer = LoginSerializer(data = data)
          print(data)
          if not serializer.is_valid():
           return Response({
               "status": False,
               "data": serializer.errors
           })
          username = serializer.data['username']
          password = serializer.data['password']

          user_obj = authenticate(username = username, password = password)
          if user_obj:
             return Response({
               "status": True,
               "data": {'token':""}
             })

          return Response({
               "status": False,
               "data": {},
               "message": "Invalid Credentials"
           })

          
     

#Retrieve All the Members

@api_view(['GET','POST'])
def retrieveAllMembers(request):

    if request.method == 'GET':
        members = Member.objects.all()
        serialized_item = MemberSerializer(members, many=True)


        return Response(serialized_item.data)

    if request.method == 'POST':
       serialized_item = MemberSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)

#Retrieve specific Member by Id
@api_view(['GET'])
def retrieveSingleMember(request,id):

    if request.method == 'GET':
        member = Member.objects.get(pk=id)

        serialized_item = MemberSerializer(member)

        return Response(serialized_item.data)


#Validate member based on MemberId, firstName and lastName sent in the URL by client app
@api_view(['GET'])
def validatelMember(request):
        
        members = Member.objects.all()

        member_id = request.query_params.get('memberId')
        first_name = request.query_params.get('firstName')
        last_name = request.query_params.get('lastName')

        if(member_id,first_name,last_name):

            if(members.filter(firstName=first_name) & members.filter(memberId=member_id) & members.filter(lastName=last_name)):
                        
                        that_member = members.filter(memberId = member_id)
                        
                        serialized_item = MemberSerializer(that_member, many=True)
                        return Response(serialized_item.data)
                 
            else:
                return HttpResponse("Member does not exist")


#Earn Rewards
@api_view(['PUT'])
def earnRewards(request,id):
   
    member = Member.objects.get(pk=id)

    if request.method == 'PUT':
       
        if (request.query_params.get('pointsEarned')):


             points_earned = request.query_params.get('pointsEarned')
         
             member.totalPoints = member.totalPoints + int(points_earned)

             member.save()

             serialized_item = MemberSerializer(member)
            
             return Response(serialized_item.data)
          
        
        else:
            return HttpResponse('Specify Points earned')
        

#Redeem Rewards
@api_view(['PUT'])
def redeemRewards(request,id):
   
    member = Member.objects.get(pk=id)

    if request.method == 'PUT':
       
        if (request.query_params.get('pointsRedeemed')):


            points_earned = request.query_params.get('pointsRedeemed')
         
            member.totalPoints = member.totalPoints - int(points_earned)

            if (member.totalPoints >= 0):

              member.save()

            else:
                 return HttpResponse('Not enough points to redeem')
                 
             

            serialized_item = MemberSerializer(member)
            
            return Response(serialized_item.data)
        
        else:
            return HttpResponse('Specify Points redeemed')
        

@api_view(['GET','POST'])
def retrieveAllMembersDetails(request):

    if request.method == 'GET':
        members = MemberDetails.objects.all()
        serialized_item = MemberDetailsSerializer(members, many=True)


        return Response(serialized_item.data)

    if request.method == 'POST':
       serialized_item = MemberDetailsSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)

#Retrieve specific Member by Id
@api_view(['GET'])
def retrieveSingleMemberDetail(request,id):

    if request.method == 'GET':
        member = MemberDetails.objects.get(pk=id)

        serialized_item = MemberDetailsSerializer(member)

        return Response(serialized_item.data)


        

