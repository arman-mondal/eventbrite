from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    user_liked = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'user', 'title', 'description', 'event_date', 'total_likes', 'user_liked']

    def get_user_liked(self, obj):
        # Check if the current authenticated user has liked the event
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False
