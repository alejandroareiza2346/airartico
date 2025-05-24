from django.db import models
from django.contrib.auth.models import User

# Create your models here.

REWARD_CHOICES = (
    ("BRONZE" , "Bronze"),
    ("GOLD" , "Gold"),
    ("PLATINUM" , "Platinum"),
)


class Member(models.Model):

    memberId = models.CharField(max_length = 10)
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    contactNumber = models.CharField(max_length = 10)
    emailAddress = models.EmailField()
    dateRegistered = models.CharField(max_length = 100)
    rewardsLevel = models.CharField(max_length=10,choices=REWARD_CHOICES, default="BRONZE")
    totalPoints = models.IntegerField(default=0)

    
    

    def __str__(self)-> str:
        return self.memberId
    
class MemberDetails(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT, default = 1)
    contactNumber = models.CharField(max_length = 10)
    emailAddress = models.EmailField()
    #dateRegistered = models.CharField(max_length = 100)
    rewardsLevel = models.CharField(max_length=10,choices=REWARD_CHOICES, default="BRONZE")
    totalPoints = models.IntegerField(default=0)

    
    

    def __str__(self)-> str:
        return self.user.username
'''
class LoyaltyProgram(models.Model):

    memberDetails = models.ForeignKey(Member, on_delete=models.PROTECT, default=1)
    rewardsLevel = models.CharField(max_length=10,choices=REWARD_CHOICES, default="BRONZE")
    totalPoints = models.IntegerField()

    def __str__(self)-> str:
        return self.memberDetails.firstName
'''