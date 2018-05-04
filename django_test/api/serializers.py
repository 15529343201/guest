from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Event, Guest

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')
		
class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')
		
class EventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('url','name','address','start_time','limit','status')
		
class GuestSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Guest
		fields = ('url','realname','phone','email','sign','event')