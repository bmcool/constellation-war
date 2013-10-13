#-*- encoding: utf-8 -*-

from django.db import models

from constellation.utils import *

from django_facebook.models import FacebookProfileModel

class Member(FacebookProfileModel):
	user = models.OneToOneField('auth.User')
	
	@property
	def constellation(self):
		return to_constellation_by_date(self.date_of_birth)

from django.contrib.auth.models import User
from django.db.models.signals import post_save

def create_facebook_profile(sender, instance, created, **kwargs):
	if created:
		Member.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=User)
