from rest_framework import serializers
from . models import User,Admin,Book_calls

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Admin
        fields = ('advisor_name', 'advisor_photo_url')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email_id','password')

class BookcallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_calls
        fields = ('advisor_name', 'advisor_profie_pic', 'advisor_id', 'book_time', 'book_id')

